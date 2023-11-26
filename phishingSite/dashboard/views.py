from django.shortcuts import render, redirect
from .models import Employee
from .models import Entreprise
from .models import Campagne
from .models import EmailCampagne
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponse
import pandas as pd
import matplotlib.pyplot as plt
from django.template import RequestContext
from django.template.loader import get_template
from .forms import EntrepriseForm

def render_chart(request):
    # Votre script pour générer le graphique
    data = pd.read_csv("static/donnees.csv")
    colonne = 'clique'
    pourcentage = data[colonne].value_counts(1) * 100

    plt.pie(pourcentage, labels=pourcentage.index, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.title('Nombre de cliques')

    # Sauvegarder le graphique en tant qu'image PNG
    plt.savefig('static/donnees.png')

    # Fermer la figure pour éviter les fuites de mémoire
    plt.close()

    # Charger le template HTML
    template = get_template('statistics.html')
    
    # Créer le contexte avec le chemin vers l'image générée
    context = {'graph_image': 'static/donnees.png'}

    # Rendre le template avec le contexte
    html = template.render(context)

    return HttpResponse(html)

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
    return render(request, 'dashboard/statisInfotics.html')

def create_campaign(request):
    if request.method == 'POST':
        form = EntrepriseForm(request.POST)
        print("POST data:", request.POST)  # Pour voir les données soumises
        if form.is_valid():
            selected_company = form.cleaned_data['entreprise']
            print("Selected company:", selected_company)  # Pour vérifier la validité des données
        else:
            print("Form errors:", form.errors)  # Pour voir les erreurs du formulaire
    else:
        form = EntrepriseForm()
    return render(request, 'dashboard/create_campaign.html', {'form': form})

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'dashboard/employee_list.html', {'employees':employees})

def phishing_mail_generator(request):
    return render(request, 'dashboard/phishing_mail_generator.html')

def phishing_page_generator(request):
    return render(request, 'dashboard/phishing_page_generator.html')

def param_admin(request):
    return render(request, 'dashboard/param_admin.html')

def info(request):
    return render(request, 'dashboard/Info.html')

def entreprise_list(request):
    entreprises = Entreprise.objects.all()
    return render(request, 'dashboard/entreprise_list.html', {'entreprises':entreprises})

def campagne_list(request):
    campagnes = Campagne.objects.all()
    return render(request, 'dashboard/campagne_list.html', {'campagnes':campagnes})

def emailcampagne_list(request):
    emailscampagne = EmailCampagne.objects.all()
    return render(request, 'dashboard/emailcampagne-list.html', {'emailscampagne':emailscampagne})
