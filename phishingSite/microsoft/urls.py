from django.urls import path
from . import views
from .views import login, submit
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("login", login, name="login"),
    path("submit", submit, name="submit"),
]