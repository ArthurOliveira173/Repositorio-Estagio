from django.contrib import admin
from .models import AlunoPcd
# Register your models here.
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('alu_nome', 'alu_cpf', 'alu_genero', 'alu_email_pessoal', 'alu_email_institucional',
                    'alu_telefone', 'alu_endereco', 'alu_matricula', 'alu_deficiencias',
                    'alu_curso', 'alu_periodo_academico', 'alu_data_nascimento')
    list_display_links = ('alu_email_pessoal', 'alu_email_institucional', 'alu_endereco')
    list_filter = ('alu_nome', 'alu_cpf')
    list_per_page = 10
    search_fields = ('alu_nome', 'alu_cpf')

admin.site.register(AlunoPcd, AlunoAdmin)