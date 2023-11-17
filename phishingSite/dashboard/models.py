from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Table contenant les entreprises
class entreprise(models.Model):
    nomEntreprise = models.CharField(max_length=200)

# Table contenant les employés de chaque entreprise
class employee(models.Model):
    nom = models.CharField(max_length=200)
    mail_address = models.EmailField()
    id_entreprise = models.ForeignKey(entreprise, on_delete=models.Cascade)

    def __str__(self):
        return self.mail_address

# Table contenant les campagnes créées par les utilisateurs
class campagne(models.Model):
    id_entreprise = models.ForeignKey(entreprise, on_delete=models.Cascade)
    mailEnvoi = models.EmailField()
    password_mailEnvoi = models.PasswordField()

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

# Table contenant la liste des emails envoés lors des campagnes
class emailCampagne(models.Model):
    id_campagne = models.ForeignKey(campagne, on_delete=models.Cascade)
    id_employee = models.ForeignKey(employee, on_delete=models.Cascade)
    clicked = models.BooleanField(default=False)
    form_completed = models.BooleanField(default=False)