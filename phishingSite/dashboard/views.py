from django.http import HttpResponse
from django.shortcuts import render
from .models import employee

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def employee_list(request):
    employees = employee.objects.all()
    return render(request, 'dashboard/employee_list.html', {'employees':employees})

def statistiques(request):
    return render(request, 'dashboard/statistiques.html')