from django.contrib import admin
from .models import Interprete
# Register your models here.

class InterpreteAdmin(admin.ModelAdmin):
    list_display = ('int_nome', 'int_cpf', 'int_genero', 'int_email_pessoal', 'int_email_institucional', 'int_telefone')
    list_display_links = ('int_nome', )
    list_filter = ('int_nome', 'int_cpf', 'int_genero')
    list_per_page = 10
    search_fields = ('int_nome', 'int_cpf', 'int_email_pessoal', 'int_email_institucional')

admin.site.register(Interprete, InterpreteAdmin)
