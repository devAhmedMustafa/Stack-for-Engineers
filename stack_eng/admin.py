from django.contrib import admin
from .models import Question, Answer, Comment, QuestionLike, AnswerLike, Save

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Comment)
admin.site.register(QuestionLike)
admin.site.register(AnswerLike)
admin.site.register(Save)