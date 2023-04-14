from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils.text import slugify

class Question(models.Model):

    title = models.CharField(max_length=200)
    question_text = models.CharField(max_length=1500)
    publisher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='question')
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/questions/%y/%m/%d', blank=True, null=True)
    subject = models.CharField(max_length=50)
    pub_date = models.DateTimeField(default= datetime.now())
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Question, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Answer(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer')
    answer_text = models.CharField(max_length=2500)
    publisher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answer')
    pub_date = models.DateTimeField(default= datetime.now())

    def count(self):
        return Answer.objects.filter(question=self.question).count()

    def __str__(self):
        return self.answer_text

class Comment(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='comment', null=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='comment')
    comment_text = models.CharField(max_length=1000)
    publisher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    pub_date = models.DateTimeField(default= datetime.now())

    def __str__(self):
        return self.comment_text
    
class QuestionLike(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_like')
    liked_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='question_like')
    like_date = models.DateTimeField(default= datetime.now())

    class Meta:
        unique_together = [('question','liked_by')]

    def __str__(self):
        return self.liked_by.username
    
class AnswerLike(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='answer_like')
    liked_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answer_like')
    like_date = models.DateTimeField(default= datetime.now())

    class Meta:
        unique_together = [('answer','liked_by')]

    def __str__(self):
        return self.liked_by.username
    
class Save(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='save')
    saved_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='save')
    save_date = models.DateTimeField(default= datetime.now())

    class Meta:
        unique_together = [('question','saved_by')]
    def __str__(self):
        return self.saved_by.username