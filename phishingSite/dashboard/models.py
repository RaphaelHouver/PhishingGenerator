import hashlib
from django.db import models
from django.contrib.auth.models import User
from .fields import HashField
from django.core.validators import MaxLengthValidator
# Create your models here.

# Table contenant les entreprises
class Entreprise(models.Model):
    nomEntreprise = models.CharField(max_length=200)

    def __str__(self):
        return self.nomEntreprise
     
# Table contenant les employés de chaque entreprise
class Employee(models.Model):
    nom = models.CharField(max_length=200)
    mail_address = models.EmailField()
    id_entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)

    def __str__(self):
        return self.mail_address

# Table contenant les campagnes créées par les utilisateurs
class Campagne(models.Model):
    id_entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    mailEnvoi = models.EmailField()
    password_mailEnvoi = HashField()

    def save(self, *args, **kwargs):
        self.password_mailEnvoi = hashlib.sha256(self.password_mailEnvoi.encode()).hexdigest()
        super().save(*args, **kwargs)

# Table contenant la liste des emails envoés lors des campagnes
class EmailCampagne(models.Model):
    id_campagne = models.ForeignKey(Campagne, on_delete=models.CASCADE)
    id_employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    clicked = models.BooleanField(default=False)
    form_completed = models.BooleanField(default=False)
    token = models.CharField(max_length=6, validators=[MaxLengthValidator(limit_value=6)])