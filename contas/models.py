from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_administrador= models.BooleanField(default=False)
    is_aluno = models.BooleanField(default=False)
    is_interprete = models.BooleanField(default=False)
    is_monitor = models.BooleanField(default=False)
    is_tutor = models.BooleanField(default=False)
    nome = models.CharField(max_length=80)
    cpf = models.CharField(max_length=20)
    sexo = models.CharField(max_length=1)
    email = models.CharField(max_length=255)

class AlunoPcd(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    alu_telefone = models.CharField(max_length=255)
    alu_matricula = models.CharField(max_length=11)
    alu_deficiencias = models.CharField(max_length=255, blank=True, null=True)
    alu_periodo_academico = models.CharField(db_column='alu_Periodo_Academico', max_length=255)  # Field name made lowercase.
    alu_data_nascimento = models.DateField()

    class Meta:
        managed = False
        db_table = 'aluno_pcd'

    def __str__(self):
        return self.alu_nome

class Administrador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    adm_nome = models.CharField(max_length=255)
    adm_cpf = models.CharField(max_length=11)
    adm_email = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'administrador'
    def __str__(self):
        return self.adm_nome

class Interprete(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    int_nome = models.CharField(max_length=255)
    int_cpf = models.CharField(max_length=11)
    int_sexo = models.CharField(max_length=1)
    int_email = models.CharField(max_length=255)
    int_telefone = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'interprete'

    def __str__(self):
        return self.int_nome

class Monitor(models.Model):
    mon_id = models.IntegerField(primary_key=True)
    mon_nome = models.CharField(max_length=255)
    mon_cpf = models.CharField(max_length=11)
    mon_sexo = models.CharField(max_length=1)
    mon_email = models.CharField(max_length=255)
    mon_telefone = models.CharField(max_length=255)
    mon_matricula = models.CharField(max_length=11)
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
    tut_periodo_academico = models.CharField(max_length=255)
    tut_tipo = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'tutor'

    def __str__(self):
        return self.tut_nome
