from django.contrib import admin
from .models import employee
from .models import campagne
from .models import entreprise
from .models import emailCampagne


admin.site.register(employee)
admin.site.register(campagne)
admin.site.register(entreprise)
admin.site.register(emailCampagne)
