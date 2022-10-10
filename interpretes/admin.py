from django.contrib import admin
from .models import Interprete
# Register your models here.

class InterpreteAdmin(admin.ModelAdmin):
    list_display = ('int_nome', 'int_cpf', 'int_sexo', 'int_email', 'int_telefone')
    list_display_links = ('int_email', 'int_cpf')
    list_filter = ('int_nome', 'int_cpf', 'int_sexo')
    list_per_page = 10
    search_fields = ('int_nome', 'int_cpf', 'int_email')

admin.site.register(Interprete, InterpreteAdmin)
