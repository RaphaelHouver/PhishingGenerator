from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class employee(models.Model):
    name = models.CharField(max_length=200)
    mail_address = models.EmailField()
    received_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mail_address
