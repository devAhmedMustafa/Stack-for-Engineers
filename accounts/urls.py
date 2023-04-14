from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.sign_up, name='sign_up'),  # type: ignore
    path('login/', views.login, name='login'), # type: ignore
    path('logout/', views.logout, name='logout'),
    path('user_validation/', views.user_validation)
]

