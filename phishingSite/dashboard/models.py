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
    
#table des mails utilisés pour envoyer les phish
class FakeEmail(models.Model):
    mail = models.EmailField()
    password = HashField()

    def save(self, *args, **kwargs):
        self.password = hashlib.sha256(self.password.encode()).hexdigest()
        super().save(*args, **kwargs)

#table contenant les templates des phishings        
class Template(models.Model):
    entreprise = models.CharField(max_length=200)
    
    def __str__(self):
        return self.entreprise
    
# Table contenant les campagnes créées par les utilisateurs
class Campagne(models.Model):
    id_entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    id_template = models.ForeignKey(Template, on_delete=models.CASCADE)
    id_mailEnvoi = models.ForeignKey(FakeEmail, on_delete=models.CASCADE)
    
# Table contenant la liste des emails envoés lors des campagnes
class EmailCampagne(models.Model):
    id_campagne = models.ForeignKey(Campagne, on_delete=models.CASCADE)
    id_employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    clicked = models.BooleanField(default=False)
    form_completed = models.BooleanField(default=False)
    token = models.CharField(max_length=6, validators=[MaxLengthValidator(limit_value=6)])

