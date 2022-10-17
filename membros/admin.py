from django.contrib import admin
from .models import Administrador, AlunoPcd, Monitor, Tutor, Interprete
# Register your models here.

class AdministradorAdmin(admin.ModelAdmin):
    list_display = ('adm_nome', 'adm_cpf', 'adm_email')
    list_display_links = ('adm_email',)
    list_filter = ('adm_nome', 'adm_cpf')
    list_per_page = 10
    search_fields = ('adm_nome', 'adm_cpf')

class AlunoAdmin(admin.ModelAdmin):
    list_display = ('alu_nome', 'alu_cpf', 'alu_genero', 'alu_email_pessoal', 'alu_email_institucional',
                    'alu_telefone', 'alu_endereco', 'alu_matricula', 'alu_deficiencias',
                    'alu_curso', 'alu_periodo_academico', 'alu_data_nascimento')
    list_display_links = ('alu_email_pessoal', 'alu_email_institucional', 'alu_endereco')
    list_filter = ('alu_nome', 'alu_cpf')
    list_per_page = 10
    search_fields = ('alu_nome', 'alu_cpf')

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

class InterpreteAdmin(admin.ModelAdmin):
    list_display = ('int_nome', 'int_cpf', 'int_genero', 'int_email_pessoal', 'int_email_institucional', 'int_telefone')
    list_display_links = ('int_nome', )
    list_filter = ('int_nome', 'int_cpf', 'int_genero')
    list_per_page = 10
    search_fields = ('int_nome', 'int_cpf', 'int_email_pessoal', 'int_email_institucional')

admin.site.register(Administrador, AdministradorAdmin)
admin.site.register(AlunoPcd, AlunoAdmin)
admin.site.register(Monitor, MonitorAdmin)
admin.site.register(Tutor, TutorAdmin)
admin.site.register(Interprete, InterpreteAdmin)
