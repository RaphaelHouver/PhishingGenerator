from django.shortcuts import render, redirect
from .models import employee
from .models import entreprise
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard/dashboard.html')
    else:
        return redirect('login')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def statistics(request):
    return render(request, 'dashboard/statistics.html')

def create_campaign(request):
    return render(request, 'dashboard/create_campaign.html')

def employee_list(request):
    employees = employee.objects.all()
    return render(request, 'dashboard/employee_list.html', {'employees':employees})
def entreprise_list(request):
    entreprises = entreprise.objects.all()
    return render(request, 'dashboard/entreprise_list.html', {'entreprises':entreprises})
def campagne_list(request):
    campagnes = campagne.objects.all()
    return render(request, 'dashboard/campagne_list.html', {'campagnes':campagnes})
    test