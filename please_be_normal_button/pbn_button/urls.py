from django.urls import path
import views

urlpatterns = [
    path("pbn_button/login", views.login)
]