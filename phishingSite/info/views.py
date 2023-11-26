from django.shortcuts import render
from django.shortcuts import get_object_or_404
from dashboard.models import EmailCampagne

def login(request, template):
    token = request.GET.get('token')
    context = {'token': token}
    #entreprise = request.GET.get('nomEntreprise')
    if token:
        instance = get_object_or_404(EmailCampagne, token=token)
        instance.clicked = True
        instance.save()
        print(f"{token} a cliqué sur le lien comme un gros nul")
    if template == "microsoft":
        return render(request, 'info/microsoft/login.html', context)
    elif template == "digiposte":
        return render(request, 'info/digiposte/login.html', context)

def submit(request, template):
    token = request.POST.get('token')
    context = {'token': token}
    if token:
        instance = get_object_or_404(EmailCampagne, token=token)
        instance.form_completed = True
        instance.save()
        print(f"{token} s'est connecté")
    if template == "microsoft":
        return render(request, 'info/microsoft/submit.html', context)
    elif template == "digiposte":
        return render(request, 'info/digiposte/submit.html', context)