from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_administrador= models.BooleanField(default=False)
    is_aluno = models.BooleanField(default=False)
    is_interprete = models.BooleanField(default=False)
    is_monitor = models.BooleanField(default=False)
    is_tutor = models.BooleanField(default=False)

class AlunoPcd(models.Model):
    user = models.OneToOneField(User, db_column='alu_id', on_delete=models.CASCADE, primary_key=True)
    nome = models.CharField(db_column='alu_nome', max_length=80)
    cpf = models.CharField(db_column='alu_cpf', max_length=20)
    sexo = models.CharField(db_column='alu_sexo', max_length=1)
    email = models.CharField(db_column='alu_email', max_length=255)
    telefone = models.CharField(db_column='alu_telefone', max_length=255)
    matricula = models.CharField(db_column='alu_matricula', max_length=11)
    deficiencias = models.CharField(db_column='alu_deficiencias', max_length=255, blank=True, null=True)
    periodo_academico = models.CharField(db_column='alu_Periodo_Academico', max_length=255)  # Field name made lowercase.
    data_nascimento = models.DateField(db_column='alu_data_nascimento')

    class Meta:
        managed = False
        db_table = 'aluno_pcd'

    def __str__(self):
        return self.nome

class Administrador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nome = models.CharField(db_column='adm_nome', max_length=255)
    cpf = models.CharField(db_column='adm_cpf', max_length=11)
    sexo = models.CharField(db_column='adm_sexo', max_length=1)
    email = models.CharField(db_column='adm_email', max_length=255)

    class Meta:
        managed = False
        db_table = 'administrador'
    def __str__(self):
        return self.nome

class Interprete(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nome = models.CharField(db_column='int_nome', max_length=255)
    cpf = models.CharField(db_column='int_cpf', max_length=11)
    sexo = models.CharField(db_column='int_sexo', max_length=1)
    email = models.CharField(db_column='int_email', max_length=255)
    telefone = models.CharField(db_column='int_telefone', max_length=255)

    class Meta:
        managed = False
        db_table = 'interprete'

    def __str__(self):
        return self.nome

class Monitor(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(db_column='mon_nome', max_length=255)
    cpf = models.CharField(db_column='mon_cpf', max_length=11)
    sexo = models.CharField(db_column='mon_sexo', max_length=1)
    email = models.CharField(db_column='mon_email', max_length=255)
    telefone = models.CharField(db_column='mon_telefone', max_length=255)
    matricula = models.CharField(db_column='mon_matricula', max_length=11)
    periodo_academico = models.CharField(db_column='mon_periodo_academico', max_length=255)
    tipo = models.CharField(db_column='mon_tipo', max_length=7)

    class Meta:
        managed = False
        db_table = 'monitor'

    def __str__(self):
        return self.nome

class Tutor(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(db_column='tut_nome', max_length=255)
    cpf = models.CharField(db_column='tut_cpf', max_length=11)
    sexo = models.CharField(db_column='tut_sexo', max_length=1)
    email = models.CharField(db_column='tut_email', max_length=255)
    telefone = models.CharField(db_column='tut_telefone', max_length=255)
    matricula = models.CharField(db_column='tut_matricula', max_length=11)
    periodo_academico = models.CharField(db_column='tut_periodo_academico', max_length=255)
    tipo = models.CharField(db_column='tut_tipo', max_length=7)

    class Meta:
        managed = False
        db_table = 'tutor'

    def __str__(self):
        return self.nome
