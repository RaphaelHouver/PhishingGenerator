from django.shortcuts import render

def login(request):
    email_campagne_id = request.GET.get('email_campagne_id')
    context = {'email_campagne_id': email_campagne_id}
    #entreprise = request.GET.get('nomEntreprise')
    if email_campagne_id:
        #email_campagne = EmailCampagne.objects.get(idEmail=email_campagne_id)
        #email_campagne.clicked = True
        #email_campagne.save()
        print(f"{email_campagne_id} a cliqué sur le lien comme un gros nul")
    return render(request, 'info/microsoft/login.html', context)

def submit(request):
    email_campagne_id = request.POST.get('email_campagne_id')
    context = {'email_campagne_id': email_campagne_id}
    if email_campagne_id:
        # email_campagne = EmailCampagne.objects.get(idEmail=email_campagne_id)
        # email_campagne.form_completed = True
        # email_campagne.save()
        print(f"{email_campagne_id} s'est connecté")
    return render(request, 'info/microsoft/submit.html', context)