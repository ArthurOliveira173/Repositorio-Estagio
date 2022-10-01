from django.contrib import admin
from .models import AlunoPcd, Administrador, Monitor, Tutor, Interprete
# Register your models here.

# class AdministradorAdmin(admin.ModelAdmin):
#     list_display = ('adm_nome', 'adm_cpf', 'adm_email')

admin.site.register(AlunoPcd)
admin.site.register(Administrador)
admin.site.register(Monitor)
admin.site.register(Tutor)
admin.site.register(Interprete)
