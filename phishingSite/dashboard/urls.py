from django.urls import path
from . import views
from .views import dashboard, employee_list, entreprise_list, campagne_list, emailcampagne_list register, statistics, create_campaign
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('register/', register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("", dashboard, name="dashboard"),
    path("statistics", statistics, name="statistics"),
    path("create-campaign", create_campaign, name="create_campaign"),
    path('employee-list', employee_list, name="employee_list"),
    path('entreprise-list/', entreprise_list, name="entreprise_list"),
    path('campagne-list/', campagne_list, name="campagne_list"),
    path('emailcampagne-list/', emailcampagne_list, name="emailcampagne_list"),
]

