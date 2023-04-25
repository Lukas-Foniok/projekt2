from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_user, name='login_user'),
    path("logout/", views.logout_user, name='logout_user'),
    path('press/', views.press_button, name= 'press_button'),
    path("", views.index, name='index')
]