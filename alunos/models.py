from django.db import models
from sistema.models import Cursos, Enderecos


# Create your models here.

generos = (
    ('M', 'Masculino'),
    ('F', 'Feminino'),
)

class AlunoPcd(models.Model):
    alu_id = models.AutoField(db_column='alu_id', primary_key=True)
    alu_nome = models.CharField(db_column='alu_nome', max_length=255)
    alu_cpf = models.CharField(db_column='alu_cpf', max_length=11)
    alu_genero = models.CharField(db_column='alu_genero', max_length=1, choices=generos)
    alu_email_pessoal = models.EmailField(db_column='alu_email_pessoal', max_length=255)
    alu_email_institucional = models.EmailField(db_column='alu_email_institucional', max_length=255)
    alu_telefone = models.CharField(db_column='alu_telefone', max_length=255)
    alu_endereco = models.ForeignKey(Enderecos, models.DO_NOTHING, db_column='alu_endereco', blank=True, null=True)
    alu_matricula = models.CharField(db_column='alu_matricula', max_length=11)
    alu_deficiencias = models.CharField(db_column='alu_deficiencias', max_length=255, blank=True, null=True)
    alu_curso = models.ForeignKey(Cursos, models.DO_NOTHING, db_column='alu_curso', blank=True, null=True)
    alu_periodo_academico = models.CharField(db_column='alu_periodo_academico', max_length=255)  # Field name made lowercase.
    alu_data_nascimento = models.DateField(db_column='alu_data_nascimento')

    class Meta:
        managed = False
        db_table = 'aluno_pcd'

    def __str__(self):
        return self.alu_nome
