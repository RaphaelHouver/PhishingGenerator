from django.shortcuts import render
from django.shortcuts import get_object_or_404
from dashboard.models import emailCampagne

def login(request):
    email_campagne_id = request.GET.get('email_campagne_id')
    context = {'email_campagne_id': email_campagne_id}
    #entreprise = request.GET.get('nomEntreprise')
    if email_campagne_id:
        instance = get_object_or_404(emailCampagne, id=email_campagne_id)
        instance.clicked = True
        instance.save()
        print(f"{email_campagne_id} a cliqué sur le lien comme un gros nul")
    return render(request, 'info/microsoft/login.html', context)

def submit(request):
    email_campagne_id = request.POST.get('email_campagne_id')
    context = {'email_campagne_id': email_campagne_id}
    if email_campagne_id:
        instance = get_object_or_404(emailCampagne, id=email_campagne_id)
        instance.form_completed = True
        instance.save()
        print(f"{email_campagne_id} s'est connecté")
    return render(request, 'info/microsoft/submit.html', context)