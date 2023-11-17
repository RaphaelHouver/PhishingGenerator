from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class employee(models.Model):
    nom = models.CharField(max_length=200)
    mail_address = models.EmailField()
    entreprise = models.CharField(max_length=200)

    def __str__(self):
        return self.mail_address

class campagne(models.Model):
    entreprise = models.CharField(max_length=200)
    mailEnvoi = models.EmailField()
    password_mailEnvoi = models.PasswordField()

class emailCampagne(models.Model):
    id_campagne = models.ForeignKey(campagne, on_delete=models.Cascade)
    id_employee = models.ForeignKey(employee, on_delete=models.Cascade)
    clicked = models.BooleanField(default=False)
    form_completed = models.BooleanField(default=False)
