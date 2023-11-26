import matplotlib
matplotlib.use('Agg')
from django.shortcuts import render, redirect
from .models import employee
from .models import entreprise
from .models import campagne
from .models import emailCampagne
from .models import template
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponse
import pandas as pd
import matplotlib.pyplot as plt
from django.template import RequestContext
from django.template.loader import get_template
from io import BytesIO
import base64
from django.db.models import Count, Q
from django.db import models

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
    return render(request, 'dashboard/statistics.html')

def create_campaign(request):
    return render(request, 'dashboard/create_campaign.html')

def employee_list(request):
    employees = employee.objects.all()
    return render(request, 'dashboard/employee_list.html', {'employees':employees})

def statistiques(request):
    return render(request, 'dashboard/statistiques.html')

def template_list(request):
    templates = template.objects.all()
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
    entreprises = entreprise.objects.all()
    return render(request, 'dashboard/entreprise_list.html', {'entreprises':entreprises})

def campagne_list(request):
    campagnes = campagne.objects.all()
    return render(request, 'dashboard/campagne_list.html', {'campagnes':campagnes})

def emailcampagne_list(request):
    emailscampagne = emailCampagne.objects.all()
    return render(request, 'dashboard/emailcampagne-list.html', {'emailscampagne':emailscampagne})

def statistics(request):
    data_clusteredbar = emailCampagne.objects.values('id_employee__id_entreprise').annotate(
        clicked_count=Count('id', filter=models.Q(clicked=True)),
        completed_count=Count('id', filter=models.Q(form_completed=True))
    )
    entreprise_names = [entry['id_employee__id_entreprise'] for entry in data_clusteredbar]
    clicked_counts = [entry['clicked_count'] for entry in data_clusteredbar]
    completed_counts = [entry['completed_count'] for entry in data_clusteredbar]

    bar_width = 0.25
    index = range(len(entreprise_names))
    plt.bar(index, clicked_counts, bar_width, label='Clicked')
    plt.bar([i + bar_width for i in index], completed_counts, bar_width, label='Completed')

    plt.xlabel('Entreprise')
    plt.ylabel('Count')
    plt.title('Grouped Bar Chart by Entreprise')
    plt.xticks([i + bar_width/2 for i in index], entreprise_names)
    plt.legend()

    # Save the plot to a BytesIO object
    image_stream = BytesIO()
    plt.savefig(image_stream, format='png')
    image_stream.seek(0)
    plt.close()

    # Encode the BytesIO object as base64 to embed in HTML
    encoded_image = base64.b64encode(image_stream.read()).decode('utf-8')

    return render(request, 'dashboard/statistics.html', {'image': encoded_image})