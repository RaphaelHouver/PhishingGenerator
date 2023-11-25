from django.urls import path
from . import views
from .views import dashboard, employee_list, register, statistics, create_campaign, phishing_mail_generator, phishing_page_generator, param_admin, Info, render_chart
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('register/', register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("", dashboard, name="dashboard"),
    path("statistics", statistics, name="statistics"),
    path("create-campaign", create_campaign, name="create_campaign"),
    path('employee-list', employee_list, name="employee_list"),
    path('phishing_mail_generator', phishing_mail_generator, name="phishing_mail_generator"),
    path('phishing_page_generator', phishing_page_generator, name="phishing_page_generator"),
    path('param_admin', param_admin, name="param_admin"),
    path('Info', Info, name="Info"),
    path('render_chart/', render_chart, name='render_chart'),
]