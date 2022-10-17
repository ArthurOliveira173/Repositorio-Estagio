from django.contrib import admin
from .models import Monitor, Tutor
# Register your models here.

class MonitorAdmin(admin.ModelAdmin):
    list_display = ('mon_nome', 'mon_cpf', 'mon_genero', 'mon_email_pessoal', 'mon_email_institucional',
                    'mon_telefone', 'mon_endereco', 'mon_matricula', 'mon_curso', 'mon_periodo_academico')
    list_display_links = ('mon_email_pessoal', 'mon_email_institucional')
    list_filter = ('mon_nome', 'mon_cpf', 'mon_genero', 'mon_curso')
    list_per_page = 10
    search_fields = ('mon_nome', 'mon_cpf', 'mon_curso')
class TutorAdmin(admin.ModelAdmin):
    list_display = ('tut_nome', 'tut_cpf', 'tut_genero', 'tut_email_pessoal', 'tut_email_institucional',
                    'tut_telefone', 'tut_endereco', 'tut_matricula', 'tut_curso', 'tut_periodo_academico')
    list_display_links = ('tut_email_pessoal', 'tut_email_institucional')
    list_filter = ('tut_nome', 'tut_cpf', 'tut_genero', 'tut_curso')
    list_per_page = 10
    search_fields = ('tut_nome', 'tut_cpf', 'tut_curso')

admin.site.register(Monitor, MonitorAdmin)
admin.site.register(Tutor, TutorAdmin)
