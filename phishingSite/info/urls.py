from django.urls import path
from . import views
from .views import login, submit
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("microsoft/login", login, {'template': 'microsoft'}, name="microsoft_login"),
    path("microsoft/submit", submit, {'template': 'microsoft'}, name="microsoft_submit"),
    path("digiposte/login", login, {'template': 'digiposte'}, name="digiposte_login"),
    path("digiposte/submit", submit, {'template': 'digiposte'}, name="digiposte_submit")
]