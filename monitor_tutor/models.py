from django.db import models
from sistema.models import Cursos
# Create your models here.

class Monitor(models.Model):
    mon_id = models.IntegerField(primary_key=True)
    mon_nome = models.CharField(max_length=255)
    mon_cpf = models.CharField(max_length=11)
    mon_sexo = models.CharField(max_length=1)
    mon_email = models.CharField(max_length=255)
    mon_telefone = models.CharField(max_length=255)
    mon_matricula = models.CharField(max_length=11)
    mon_curso = models.ForeignKey(Cursos, models.DO_NOTHING, db_column='mon_curso', blank=True, null=True)
    mon_periodo_academico = models.CharField(max_length=255)
    mon_tipo = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'monitor'

    def __str__(self):
        return self.mon_nome
class Tutor(models.Model):
    tut_id = models.IntegerField(primary_key=True)
    tut_nome = models.CharField(max_length=255)
    tut_cpf = models.CharField(max_length=11)
    tut_sexo = models.CharField(max_length=1)
    tut_email = models.CharField(max_length=255)
    tut_telefone = models.CharField(max_length=255)
    tut_matricula = models.CharField(max_length=11)
    tut_curso = models.ForeignKey(Cursos, models.DO_NOTHING, db_column='tut_curso', blank=True, null=True)
    tut_periodo_academico = models.CharField(max_length=255)
    tut_tipo = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'tutor'
    def __str__(self):
        return self.tut_nome

