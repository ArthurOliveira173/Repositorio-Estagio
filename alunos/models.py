from django.db import models

# from sistema.models. import Cursos, Disciplinas
# from django.contrib.auth.models import AbstractUser
#
# # Create your models here.
# class User(AbstractUser):
#     is_administrador= models.BooleanField(default=False)
#     is_aluno = models.BooleanField(default=False)
#     is_interpretes = models.BooleanField(default=False)
#     is_monitor = models.BooleanField(default=False)
#     is_tutor = models.BooleanField(default=False)
#     nome = models.CharField(max_length=80)
#     cpf = models.CharField(max_length=20)
#     sexo = models.CharField(max_length=1)
#     email = models.CharField(max_length=255)
#
# class AlunoPcd(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     alu_telefone = models.CharField(max_length=255)
#     alu_matricula = models.CharField(max_length=11)
#     alu_deficiencias = models.CharField(max_length=255, blank=True, null=True)
#     alu_cur = models.ForeignKey(Cursos, models.DO_NOTHING, blank=True, null=True)
#     alu_dis = models.ForeignKey(Disciplinas, models.DO_NOTHING, blank=True, null=True)
#     alu_periodo_academico = models.CharField(db_column='alu_Periodo_Academico', max_length=255)  # Field name made lowercase.
#     alu_data_nascimento = models.DateField()
#
#     class Meta:
#         managed = False
#         db_table = 'aluno_pcd'
#
#     def __str__(self):
#         return self.alu_nome

from sistema.models import Cursos, Disciplinas


# Create your models here.

class AlunoPcd(models.Model):
    alu_id = models.IntegerField(db_column='alu_id', primary_key=True)
    alu_nome = models.CharField(db_column='alu_nome', max_length=255)
    alu_cpf = models.CharField(db_column='alu_cpf', max_length=11)
    alu_sexo = models.CharField(db_column='alu_sexo', max_length=1)
    alu_email = models.CharField(db_column='alu_email', max_length=255)
    alu_telefone = models.CharField(db_column='alu_telefone', max_length=255)
    alu_matricula = models.CharField(db_column='alu_matricula', max_length=11)
    alu_deficiencias = models.CharField(db_column='alu_deficiencias', max_length=255, blank=True, null=True)
    alu_curso = models.ForeignKey(Cursos, models.DO_NOTHING, db_column='alu_curso', blank=True, null=True)
    alu_periodo_academico = models.CharField(db_column='alu_Periodo_Academico', max_length=255)  # Field name made lowercase.
    alu_data_nascimento = models.DateField(db_column='alu_data_nascimento')

    class Meta:
        managed = False
        db_table = 'aluno_pcd'

    def __str__(self):
        return self.alu_nome
