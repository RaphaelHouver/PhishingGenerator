import hashlib
from django.db import models
from django.contrib.auth.models import User
from .fields import HashField
from django.core.validators import MaxLengthValidator


# Table contenant les entreprises
class entreprise(models.Model):
    nomEntreprise = models.CharField(max_length=200)

# table contenant les templates des phishing
class template(models.Model):
    entreprise = models.CharField(max_length=200)

# Table contenant les employés de chaque entreprise
class employee(models.Model):
    nom = models.CharField(max_length=200)
    mail_address = models.EmailField()
    id_entreprise = models.ForeignKey(entreprise, on_delete=models.CASCADE)

    def __str__(self):
        return self.mail_address

#table des mails utilisés pour envoyer les phish
class fakeEmail(models.Model):
    mail = models.EmailField()
    password = HashField()

    def save(self, *args, **kwargs):
        self.password = hashlib.sha256(self.password.encode()).hexdigest()
        super().save(*args, **kwargs)

# Table contenant les campagnes créées par les utilisateurs
class campagne(models.Model):
    id_entreprise = models.ForeignKey(entreprise, on_delete=models.CASCADE)
    id_template = models.ForeignKey(template, on_delete=models.CASCADE)
    id_mailEnvoi = models.ForeignKey(fakeEmail, on_delete=models.CASCADE)

# Table contenant la liste des emails envoyés lors des campagnes
class emailCampagne(models.Model):
    id_campagne = models.ForeignKey(campagne, on_delete=models.CASCADE)
    id_employee = models.ForeignKey(employee, on_delete=models.CASCADE)
    clicked = models.BooleanField(default=False)
    form_completed = models.BooleanField(default=False)
    token = models.CharField(max_length=6, validators=[MaxLengthValidator(limit_value=6)])

