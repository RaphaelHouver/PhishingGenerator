from django.urls import path
from dashboard.views import dashboard, employee_list, entreprise_list, campagne_list, emailcampagne_list, register, statistics, create_campaign, phishing_mail_generator, phishing_page_generator, param_admin, info, render_chart
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('register', register, name='register'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path("", dashboard, name="dashboard"),
    path("statistics", statistics, name="statistics"),
    path("create-campaign", create_campaign, name="create_campaign"),
    path('phishing-mail-generator', phishing_mail_generator, name="phishing_mail_generator"),
    path("phishing-page-generator", phishing_page_generator, name="phishing_page_generator"),
    path("param-admin", param_admin, name="param_admin"),
    path('employee-list', employee_list, name="employee_list"),
    path('entreprise-list', entreprise_list, name="entreprise_list"),
    path('campagne-list', campagne_list, name="campagne_list"),
    path('emailcampagne-list', emailcampagne_list, name="emailcampagne_list"),
    path('info', info, name="info")
]

