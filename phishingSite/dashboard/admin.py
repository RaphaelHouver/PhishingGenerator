from django.contrib import admin
from .models import employee
from .models import campagne
from .models import entreprise
from .models import emailCampagne
from .models import template
from .models import fakeEmail

# class campagneAdmin(admin.ModelAdmin):
#     list_display = ('id', 'id_entreprise', 'mailEnvoi', 'password_mailEnvoi', 'custom_edit_link')
#     def custom_edit_link(self, obj):
#         return f'<a href="/admin/dashboard/campagne/{obj.id}/change/">Edit</a>'

#     custom_edit_link.allow_tags = True
#     custom_edit_link.short_description = 'Edit Link'

admin.site.register(employee)
# admin.site.register(campagne, campagneAdmin)
admin.site.register(campagne)
admin.site.register(entreprise)
admin.site.register(template)
admin.site.register(emailCampagne)
admin.site.register(fakeEmail)
