from django.urls import path
from . import views
from .views import employee_list

urlpatterns = [
    path("", views.index, name="index"),
    path('employee-list/', employee_list, name="employee_list"),
]