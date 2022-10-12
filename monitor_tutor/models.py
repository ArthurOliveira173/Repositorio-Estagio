from django.db import models
from sistema.models import Cursos, Enderecos
# Create your models here.

class Monitor(models.Model):
    mon_id = models.AutoField(db_column='mon_id', primary_key=True)
    mon_nome = models.CharField(db_column='mon_nome', max_length=255)
    mon_cpf = models.CharField(db_column='mon_cpf', max_length=11)
    mon_genero = models.CharField(db_column='mon_genero', max_length=1)
    mon_email_pessoal = models.EmailField(db_column='mon_email_pessoal', max_length=255)
    mon_email_institucional = models.EmailField(db_column='mon_email_institucional', max_length=255)
    mon_telefone = models.CharField(db_column='mon_telefone', max_length=255)
    mon_endereco = models.ForeignKey(Enderecos, models.DO_NOTHING, db_column='mon_endereco', blank=True, null=True)
    mon_matricula = models.CharField(db_column='mon_matricula', max_length=11)
    mon_curso = models.ForeignKey(Cursos, models.DO_NOTHING, db_column='mon_curso', blank=True, null=True)
    mon_periodo_academico = models.CharField(db_column='mon_periodo_academico', max_length=255)
    mon_tipo = models.CharField(db_column='mon_tipo', max_length=7)

    class Meta:
        managed = False
        db_table = 'monitor'

    def __str__(self):
        return self.mon_nome

class Tutor(models.Model):
    tut_id = models.AutoField(db_column='tut_id', primary_key=True)
    tut_nome = models.CharField(db_column='tut_nome', max_length=255)
    tut_cpf = models.CharField(db_column='tut_cpf', max_length=11)
    tut_genero = models.CharField(db_column='tut_genero', max_length=1)
    tut_email_pessoal = models.EmailField(db_column='tut_email_pessoal', max_length=255)
    tut_email_institucional = models.EmailField(db_column='tut_email_institucional', max_length=255)
    tut_telefone = models.CharField(db_column='tut_telefone', max_length=255)
    tut_endereco = models.ForeignKey(Enderecos, models.DO_NOTHING, db_column='tut_endereco', blank=True, null=True)
    tut_matricula = models.CharField(db_column='tut_matricula', max_length=11)
    tut_curso = models.ForeignKey(Cursos, models.DO_NOTHING, db_column='tut_curso', blank=True, null=True)
    tut_periodo_academico = models.CharField(db_column='tut_periodo_academico', max_length=255)
    tut_tipo = models.CharField(db_column='tut_tipo', max_length=7)

    class Meta:
        managed = False
        db_table = 'tutor'
    def __str__(self):
        return self.tut_nome

