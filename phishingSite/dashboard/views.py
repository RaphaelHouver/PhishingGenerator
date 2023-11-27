import matplotlib
matplotlib.use('Agg')
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
from io import BytesIO
import base64
from django.db.models import Count, Q, F
from django.db import models
import csv
import numpy as np

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

def statistiques(request):
    return render(request, 'dashboard/statistiques.html')

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

def statistics(request):
    #Graph clustered bar goupé par entreprise 
    data_clusteredbar = EmailCampagne.objects.values('id_employee__id_entreprise__nomEntreprise').annotate(
        clicked_count=Count('id', filter=models.Q(clicked=True)),
        completed_count=Count('id', filter=models.Q(form_completed=True))
    )
    entreprise_names = [entry['id_employee__id_entreprise__nomEntreprise'] for entry in data_clusteredbar]
    clicked_counts = [entry['clicked_count'] for entry in data_clusteredbar]
    completed_counts = [entry['completed_count'] for entry in data_clusteredbar]

    bar_width = 0.22
    gap = 0.1
    index = np.arange(len(entreprise_names))
    colors = ['lightcoral', 'lightblue']

    plt.bar(index - gap/2, clicked_counts, bar_width, label='Clics', color='lightblue')
    plt.bar([i + bar_width for i in index], completed_counts, bar_width, label='Complétions', color='lightcoral')

    plt.xlabel('Entreprise')
    plt.ylabel('Somme')
    plt.title('Répartition d\'interaction par Entreprise')
    plt.xticks([(i - gap/2) + bar_width/2 for i in index], entreprise_names)
    plt.legend()

    clustered_image_stream = BytesIO()
    plt.savefig(clustered_image_stream, format='png')
    clustered_image_stream.seek(0)
    plt.close()

    clusteredbar_image = base64.b64encode(clustered_image_stream.read()).decode('utf-8')
    #Evolution graph par campagne
    # data_evolution = EmailCampagne.objects.values('id_employee__id_entreprise__nomEntreprise', 'id_campagne').annotate(
    #     form_completed_count=Count('id', filter=models.Q(form_completed=True))
    # )

    # entreprise_names = [entry['id_employee__id_entreprise__nomEntreprise'] for entry in data_clusteredbar]
    # clicked_counts = [entry['clicked_count'] for entry in data_clusteredbar]
    # completed_counts = [entry['completed_count'] for entry in data_clusteredbar]
    # entreprises = set(entry['id_employee__id_entreprise__nomEntreprise'] for entry in data_evolution)
    # plt.figure(figsize=(8, 4.8))
    
    # for entreprise in entreprises:
    #     entreprise_data = [entry for entry in data_evolution if entry['id_employee__id_entreprise__nomEntreprise'] == entreprise]
    #     id_campagnes = [entry['id_campagne'] for entry in entreprise_data]
    #     form_completed_counts = [entry['form_completed_count'] for entry in entreprise_data]
    #     plt.plot(id_campagnes, form_completed_counts, label=entreprise, marker='o', linestyle='-', markersize=8)
    
    # plt.xlabel('Numéro de campagne')
    # plt.ylabel('Nombre de formulaires complétés')
    # plt.title('Evolution des formulaires complétés par campagne')
    # plt.legend()

    # evolution_image_stream = BytesIO()
    # plt.savefig(evolution_image_stream, format='png')
    # evolution_image_stream.seek(0)
    # plt.close()

    # evolutionbar_image = base64.b64encode(evolution_image_stream.read()).decode('utf-8')

    #Pie chart for each enterprise

    enterprises = EmailCampagne.objects.values('id_employee__id_entreprise__nomEntreprise').distinct()
    piechart_images = []
    for enterprise in enterprises:
        enterprise_name = enterprise['id_employee__id_entreprise__nomEntreprise']
        
        clicked_count = EmailCampagne.objects.filter(id_employee__id_entreprise__nomEntreprise=enterprise_name, clicked=True).count()
        form_completed_count = EmailCampagne.objects.filter(id_employee__id_entreprise__nomEntreprise=enterprise_name, form_completed=True).count()
        total_count = EmailCampagne.objects.filter(id_employee__id_entreprise__nomEntreprise=enterprise_name).count()
        difference_count = total_count - clicked_count

        plt.figure(figsize=(6, 6))
        labels = ['Cliqués', 'Remplis', 'Non cliqués']
        sizes = [clicked_count, form_completed_count, difference_count]
        colors = ['lightcoral', 'mediumaquamarine', 'lightblue']

        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
        plt.title(f'Pie Chart for {enterprise_name}')
        
        pie_chart_image_stream = BytesIO()
        plt.savefig(pie_chart_image_stream, format='png')
        pie_chart_image_stream.seek(0)
        plt.close()
        piechart_image = base64.b64encode(pie_chart_image_stream.read()).decode('utf-8')
        piechart_images.append(piechart_image)

    return render(request, 'dashboard/statistics.html', {'clusteredbar': clusteredbar_image, 'piecharts' : piechart_images})


def export_stats(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="statistiques.csv"'

    writer = csv.writer(response)
    writer.writerow(['Campagne', 'Liens cliques', 'Formulaires remplis', 'Entreprise', 'Total de mails envoyes'])

    data = EmailCampagne.objects.values('id_campagne').annotate(
        clicked_count=Count('id', filter=Q(clicked=True)),
        form_completed_count=Count('id', filter=Q(form_completed=True)),
        entreprise_name=F('id_employee__id_entreprise__nomEntreprise'),
        total_count=Count('id')
    ).order_by('id_campagne')

    for entry in data:
        writer.writerow([entry['id_campagne'], entry['clicked_count'], entry['form_completed_count'], entry['entreprise_name'], entry['total_count']])

    return response