from django.contrib import admin
from .models import Employee
from .models import Campagne
from .models import Entreprise
from .models import EmailCampagne



admin.site.register(Employee)
admin.site.register(Campagne)
admin.site.register(Entreprise)
admin.site.register(EmailCampagne)
