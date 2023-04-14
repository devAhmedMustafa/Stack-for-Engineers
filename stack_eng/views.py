from django.shortcuts import render, redirect
from .serializers import *
from .models import Question, Answer, Comment, QuestionLike, AnswerLike, Save
from django.db.models import Count
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


def home(request):

    user = request.user

    questions = Question.objects.annotate(number_of_answers=Count('answer', distinct=True), num_of_likes=Count('question_like', distinct=True))
    
    return render(request, 'home.html', {'user':user, 'questions':questions})

@login_required
def question(request, pk):

    user = request.user

    question = Question.objects.get(pk=pk)
    answers = Answer.objects.filter(question=question).annotate(number_of_comments=Count('comment')).annotate(num_of_likes=Count('answer_like'))
    answersCounter = answers.count()
    comments = Comment.objects.filter(question=question)

    qlikes = QuestionLike.objects.filter(question=question)
    qlikesCounter = qlikes.count()

    alike = AnswerLike.objects.filter(question=question, liked_by=user)

    question_like = QuestionLike.objects.filter(question=question, liked_by = user).exists()

    save_status = False
    if Save.objects.filter(question=question, saved_by=user):
        save_status=True

    return render(request, 'question.html',
        {'question':question, 
        'answers':answers, 
        'answersCount':answersCounter, 
        'comments':comments, 
        'num_of_qlikes':qlikesCounter, 
        'question_like':question_like,
        'answer_like': alike,
        'save_status':save_status
        }
    )

@login_required
def add_question(request):

    user = request.user

    if request.method == 'POST':

        title = request.POST['title']
        question_text = request.POST['question_text']
        subject = request.POST['subject']

        question = Question(publisher=user, title=title, question_text=question_text, subject=subject)
        question.save()
        
        return redirect('home')

    return render(request, 'add_question.html')

@login_required
def post_answer(request):

    user = request.user
    answer_text = request.GET.get('answer')
    pk = request.GET.get('pk')
    question = Question.objects.get(pk=pk)

    Answer.objects.create(
        publisher=user, 
        answer_text=answer_text, 
        question=question
    )

    data = {
    }
    
    return JsonResponse(data)

@login_required
def post_comment(request):

    user = request.user
    comment_text = request.GET.get('comment')
    pk = request.GET.get('pk')
    answer = Answer.objects.get(pk=pk)
    print(pk)
    print(comment_text)

    comment = Comment(
        publisher=user, 
        comment_text=comment_text, 
        question= answer.question,
        answer=answer,
    )
    comment.save()

    data = {
    }
    
    return JsonResponse(data)

@login_required
def saves(request):

    status = request.GET.get('status')
    pk = request.GET.get('pk')
    print(pk)

    if status == 'unsaved':
        Save.objects.create(
            saved_by=request.user,
            question=Question.objects.get(pk=pk)
        )

    else:
        Save.objects.filter(saved_by=request.user, question=Question.objects.get(pk=pk)).delete()

    data ={}

    return JsonResponse(data)

@login_required
def reactions(request):

    status = request.GET.get('status')
    pk = request.GET.get('pk')

    if status == 'unliked':
        like = QuestionLike(
            liked_by=request.user, 
            question=Question.objects.get(pk=pk),
        )

        like.save()

    else:
        QuestionLike.objects.filter(liked_by=request.user, question=Question.objects.get(pk=pk)).delete()

    data ={}

    return JsonResponse(data)

@login_required
def answer_reactions(request):

    status = request.GET.get('status')
    pk = request.GET.get('pk')
    answer = Answer.objects.get(pk=pk)

    if status == 'unliked':
        like = AnswerLike(
            liked_by=request.user, 
            question=Question.objects.get(answer=answer),
            answer=answer
        )

        like.save()

    else:
        AnswerLike.objects.filter(liked_by=request.user, answer=answer).delete()

    data ={}

    return JsonResponse(data)

@login_required
def get_like_status(request):

    pk = request.GET.get('pk')
    user = request.user
    answer = Answer.objects.get(pk=pk)

    likeStatus = 'unliked'
    if AnswerLike.objects.filter(answer=answer, liked_by=user).exists():
        likeStatus = 'liked'

    data = {
        'likeStatus':likeStatus,
    }

    return JsonResponse(data)
