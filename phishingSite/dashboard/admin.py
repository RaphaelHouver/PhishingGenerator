from django.contrib import admin
from .models import Employee
from .models import Campagne
from .models import Entreprise
from .models import EmailCampagne
from .models import Template
from .models import FakeEmail


#     custom_edit_link.allow_tags = True
#     custom_edit_link.short_description = 'Edit Link'

admin.site.register(Employee)
admin.site.register(Campagne)
admin.site.register(Entreprise)
admin.site.register(EmailCampagne)
admin.site.register(Template)
admin.site.register(FakeEmail)
