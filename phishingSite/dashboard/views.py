from django.shortcuts import render, redirect
from .models import Employee
from .models import Entreprise
from .models import Campagne
from .models import EmailCampagne
from .models import Template
from .models import FakeEmail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponse
import pandas as pd
import matplotlib.pyplot as plt
from django.template import RequestContext
from django.template.loader import get_template
from .forms import CampaignForm
from .mail import *
import random

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
        campaign_form = CampaignForm(request.POST)
        print("POST data:", request.POST)  # Pour voir les données soumises
        if campaign_form.is_valid():
            selected_company = campaign_form.cleaned_data['entreprise']
            selected_template = campaign_form.cleaned_data['template']
            print(f"Selected company: {selected_company}")  # Pour vérifier la validité des données
            print(f"Selected template: '{selected_template}'")  # Pour vérifier la validité des données
            employees = Employee.objects.filter(id_entreprise__nomEntreprise=selected_company)
            for employee in employees:
                new_token = random.randint(0,100000)
                print(employee.nom)
                print(type(selected_template))
                if selected_template.entreprise == "Microsoft":
                    sendmailsMicrosoft(employee.nom, employee.mail_address, new_token)
                    id_mailEnvoi = FakeEmail.objects.get(id=1) 
                if selected_template.entreprise == "Digiposte":
                    sendmailsDigipost(employee.nom, employee.mail_address, new_token)
                    id_mailEnvoi = FakeEmail.objects.get(id=2) 
                print(f"Mail {selected_template.entreprise} envoyé à {employee.nom}")
                nouvelle_campagne = Campagne(
                    id_entreprise=selected_company,
                    id_mailEnvoi=id_mailEnvoi,
                    id_template=selected_template
                )
                nouvelle_campagne.save()
                nouveau_mail = EmailCampagne(
                    clicked=False,
                    form_completed=False,
                    token=new_token,
                    id_campagne=nouvelle_campagne,
                    id_employee=employee,
                )
                nouveau_mail.save()
                
                    
            
        else:
            print("Form errors:", campaign_form.errors)  # Pour voir les erreurs du formulaire
    else:
        campaign_form = CampaignForm()
    return render(request, 'dashboard/create_campaign.html', {'campaign_form': campaign_form})

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'dashboard/employee_list.html', {'employees':employees})

def template_list(request):
    templates = Template.objects.all()
    return render(request, 'dashboard/template_list.html', {'templates':templates})

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
