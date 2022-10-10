from django.contrib import admin
from .models import Monitor, Tutor
# Register your models here.

class MonitorAdmin(admin.ModelAdmin):
    list_display = ('mon_nome', 'mon_cpf', 'mon_sexo', 'mon_email',
                    'mon_telefone', 'mon_matricula', 'mon_curso', 'mon_periodo_academico',
                    'mon_tipo')
    list_display_links = ('mon_email', 'mon_nome')
    list_filter = ('mon_nome', 'mon_cpf', 'mon_sexo', 'mon_curso')
    list_per_page = 10
    search_fields = ('mon_nome', 'mon_cpf', 'mon_curso')
class TutorAdmin(admin.ModelAdmin):
    list_display = ('tut_nome', 'tut_cpf', 'tut_sexo', 'tut_email',
                    'tut_telefone', 'tut_matricula', 'tut_curso', 'tut_periodo_academico',
                    'tut_tipo')
    list_display_links = ('tut_email', 'tut_nome')
    list_filter = ('tut_nome', 'tut_cpf', 'tut_sexo', 'tut_curso')
    list_per_page = 10
    search_fields = ('tut_nome', 'tut_cpf', 'tut_curso')

admin.site.register(Monitor, MonitorAdmin)
admin.site.register(Tutor, TutorAdmin)
