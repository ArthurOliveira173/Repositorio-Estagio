from django.contrib import admin
from .models import Administrador
# Register your models here.

class AdministradorAdmin(admin.ModelAdmin):
    list_display = ('adm_nome', 'adm_cpf', 'adm_email')
    list_display_links = ('adm_email',)
    list_filter = ('adm_nome', 'adm_cpf')
    list_per_page = 10
    search_fields = ('adm_nome', 'adm_cpf')
admin.site.register(Administrador, AdministradorAdmin)
