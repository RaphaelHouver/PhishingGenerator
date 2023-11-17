from django.urls import path
from . import views
from .views import dashboard, employee_list, register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('register/', register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("", dashboard, name="dashboard"),
    path('employee-list/', employee_list, name="employee_list"),
]