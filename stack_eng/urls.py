from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('<int:pk>/', views.question, name='question'),
    path('ask/', views.add_question, name='ask'),

    #ajax requests
    path('post_answer/', views.post_answer),
    path('post_comment/', views.post_comment),
    path('api_reactions', views.reactions),
    path('get_like_status/', views.get_like_status),
    path('api_answer_reaction/', views.answer_reactions),
    path('api_saves/', views.saves),

]