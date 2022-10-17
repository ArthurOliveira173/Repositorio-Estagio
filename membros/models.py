from django.db import models
from sistema.models import Cursos, Enderecos

generos = (
    ('M', 'Masculino'),
    ('F', 'Feminino'),
)

# Create your models here.

class Administrador(models.Model):
    adm_id = models.AutoField(db_column='adm_id', primary_key=True)
    adm_nome = models.CharField(db_column='adm_nome', max_length=255)
    adm_cpf = models.CharField(db_column='adm_cpf', max_length=11)
    adm_email = models.EmailField(db_column='adm_email', max_length=255)

    class Meta:
        managed = False
        db_table = 'administrador'
    def __str__(self):
        return self.adm_nome

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

class Monitor(models.Model):
    mon_id = models.AutoField(db_column='mon_id', primary_key=True)
    mon_nome = models.CharField(db_column='mon_nome', max_length=255)
    mon_cpf = models.CharField(db_column='mon_cpf', max_length=11)
    mon_genero = models.CharField(db_column='mon_genero', max_length=1, choices=generos)
    mon_email_pessoal = models.EmailField(db_column='mon_email_pessoal', max_length=255)
    mon_email_institucional = models.EmailField(db_column='mon_email_institucional', max_length=255)
    mon_telefone = models.CharField(db_column='mon_telefone', max_length=255)
    mon_endereco = models.ForeignKey(Enderecos, models.DO_NOTHING, db_column='mon_endereco', blank=True, null=True)
    mon_matricula = models.CharField(db_column='mon_matricula', max_length=11)
    mon_curso = models.ForeignKey(Cursos, models.DO_NOTHING, db_column='mon_curso', blank=True, null=True)
    mon_periodo_academico = models.CharField(db_column='mon_periodo_academico', max_length=255)

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

    class Meta:
        managed = False
        db_table = 'tutor'
    def __str__(self):
        return self.tut_nome

class Interprete(models.Model):
    int_id = models.AutoField(db_column='int_id', primary_key=True)
    int_nome = models.CharField(db_column='int_nome', max_length=255)
    int_cpf = models.CharField(db_column='int_cpf', max_length=11)
    int_genero = models.CharField(db_column='int_genero', max_length=1, choices=generos)
    int_email_pessoal = models.EmailField(db_column='int_email_pessoal', max_length=255)
    int_email_institucional = models.EmailField(db_column='int_email_institucional', max_length=255)
    int_telefone = models.CharField(db_column='int_telefone', max_length=255)

    class Meta:
        managed = False
        db_table = 'interprete'
    def __str__(self):
        return self.int_nome