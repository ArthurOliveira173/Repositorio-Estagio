from django.db import models

from sistema.models import Cursos, Disciplinas


# Create your models here.

class AlunoPcd(models.Model):
    alu_id = models.IntegerField(primary_key=True)
    alu_nome = models.CharField(max_length=255)
    alu_cpf = models.CharField(max_length=11)
    alu_sexo = models.CharField(max_length=1)
    alu_email = models.CharField(max_length=255)
    alu_telefone = models.CharField(max_length=255)
    alu_matricula = models.CharField(max_length=11)
    alu_deficiencias = models.CharField(max_length=255, blank=True, null=True)
    alu_cur = models.ForeignKey(Cursos, models.DO_NOTHING, blank=True, null=True)
    alu_dis = models.ForeignKey(Disciplinas, models.DO_NOTHING, blank=True, null=True)
    alu_periodo_academico = models.CharField(db_column='alu_Periodo_Academico', max_length=255)  # Field name made lowercase.
    alu_data_nascimento = models.DateField()

    class Meta:
        managed = False
        db_table = 'aluno_pcd'

    def __str__(self):
        return self.alu_nome