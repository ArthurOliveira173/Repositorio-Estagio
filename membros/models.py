from django.db import models
from sistema.models import Cursos
from django.contrib.auth.models import User
generos = (
    ('M', 'Masculino'),
    ('F', 'Feminino'),
    ('O', 'Outros'),
)
cidades = (
    #Código na SEF-MG
    ('01', 'Assis Brasil'),
    ('02', 'Brasileia'),
    ('03', 'Cruzeiro Do Sul'),
    ('04', 'Feijo'),
    ('05', 'Mancio Lima'),
    ('06', 'Manoel Urbano'),
    ('07', 'Placido De Castro'),
    ('08', 'Rio Branco'),
    ('09', 'Sena Madureira'),
    ('10', 'Senador Guiomard'),
    ('11', 'Tarauaca'),
    ('12', 'Xapuri'),
    ('13', 'Acrelandia'),
    ('14', 'Bujari'),
    ('15', 'Capixaba'),
    ('16', 'Epitaciolandia'),
    ('17', 'Jordão'),
    ('18', 'Marechal Thaumaturgo'),
    ('19', 'Porto Acre'),
    ('20', 'Porto Walter'),
    ('21', 'Rodrigues Alvez'),
    ('22', 'Santa Rosa Do Purus'),
)

periodos = (
    ('1', '1º Período'),
    ('2', '2º Período'),
    ('3', '3º Período'),
    ('4', '4º Período'),
    ('5', '5º Período'),
    ('6', '6º Período'),
    ('7', '7º Período'),
    ('8', '8º Período'),
    ('9', '9º Período'),
    ('10', '10º Período'),
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
    alu_user = models.OneToOneField(User, db_column='alu_user', on_delete=models.CASCADE)
    alu_nome = models.CharField(db_column='alu_nome', max_length=255)
    alu_cpf = models.CharField(db_column='alu_cpf', max_length=11, verbose_name='cpf')
    alu_genero = models.CharField(db_column='alu_genero', max_length=1, choices=generos)
    alu_email_pessoal = models.EmailField(db_column='alu_email_pessoal', max_length=255)
    alu_email_institucional = models.EmailField(db_column='alu_email_institucional', max_length=255, verbose_name='email_inst')
    alu_telefone = models.CharField(db_column='alu_telefone', max_length=255)
    alu_endereco_cep = models.CharField(db_column='alu_endereco_cep', max_length=255)
    alu_endereco_descricao = models.CharField(db_column='alu_endereco_descricao', max_length=255)
    alu_endereco_cidade = models.CharField(db_column='alu_endereco_cidade', max_length=255, choices=cidades)
    alu_matricula = models.CharField(db_column='alu_matricula', max_length=11)
    alu_deficiencias = models.CharField(db_column='alu_deficiencias', max_length=255, blank=True, null=True)
    alu_curso = models.ForeignKey(Cursos, on_delete=models.PROTECT, db_column='alu_curso', blank=True, null=True)
    alu_periodo_academico = models.CharField(db_column='alu_periodo_academico', max_length=255, choices=periodos)  # Field name made lowercase.
    alu_data_nascimento = models.DateField(db_column='alu_data_nascimento')
    alu_ativo = models.BooleanField(db_column="alu_ativo", default=False)

    class Meta:
        managed = False
        db_table = 'aluno_pcd'

    def __str__(self):
        return self.alu_nome

    def ativar(self):
        self.alu_ativo = True
        self.save()

    def desativar(self):
        self.alu_ativo = False
        self.save()

class Monitor(models.Model):
    mon_id = models.AutoField(db_column='mon_id', primary_key=True)
    mon_user = models.OneToOneField(User, db_column='mon_user', on_delete=models.CASCADE)
    mon_nome = models.CharField(db_column='mon_nome', max_length=255)
    mon_cpf = models.CharField(db_column='mon_cpf', max_length=11)
    mon_genero = models.CharField(db_column='mon_genero', max_length=1, choices=generos)
    mon_email_pessoal = models.EmailField(db_column='mon_email_pessoal', max_length=255)
    mon_email_institucional = models.EmailField(db_column='mon_email_institucional', max_length=255)
    mon_telefone = models.CharField(db_column='mon_telefone', max_length=255)
    mon_endereco_cep = models.CharField(db_column='mon_endereco_cep', max_length=255)
    mon_endereco_descricao = models.CharField(db_column='mon_endereco_descricao', max_length=255)
    mon_endereco_cidade = models.CharField(db_column='mon_endereco_cidade', max_length=255, choices=cidades)
    mon_matricula = models.CharField(db_column='mon_matricula', max_length=11)
    mon_curso = models.ForeignKey(Cursos, models.DO_NOTHING, db_column='mon_curso', blank=True, null=True)
    mon_periodo_academico = models.CharField(db_column='mon_periodo_academico', max_length=255)
    mon_ativo = models.BooleanField(db_column="mon_ativo", default=False)

    class Meta:
        managed = False
        db_table = 'monitor'

    def __str__(self):
        return self.mon_nome

    def ativar(self):
        self.mon_ativo = True
        self.save()

    def desativar(self):
        self.mon_ativo = False
        self.save()

class Tutor(models.Model):
    tut_id = models.AutoField(db_column='tut_id', primary_key=True)
    tut_user = models.OneToOneField(User, db_column='tut_user', on_delete=models.CASCADE)

    tut_nome = models.CharField(db_column='tut_nome', max_length=255)
    tut_cpf = models.CharField(db_column='tut_cpf', max_length=11)
    tut_genero = models.CharField(db_column='tut_genero', max_length=1, choices=generos)
    tut_email_pessoal = models.EmailField(db_column='tut_email_pessoal', max_length=255)
    tut_email_institucional = models.EmailField(db_column='tut_email_institucional', max_length=255)
    tut_telefone = models.CharField(db_column='tut_telefone', max_length=255)
    tut_endereco_cep = models.CharField(db_column='tut_endereco_cep', max_length=255)
    tut_endereco_descricao = models.CharField(db_column='tut_endereco_descricao', max_length=255)
    tut_endereco_cidade = models.CharField(db_column='tut_endereco_cidade', max_length=255, choices=cidades)
    tut_matricula = models.CharField(db_column='tut_matricula', max_length=11)
    tut_curso = models.ForeignKey(Cursos, models.DO_NOTHING, db_column='tut_curso', blank=True, null=True)
    tut_periodo_academico = models.CharField(db_column='tut_periodo_academico', max_length=255)
    tut_ativo = models.BooleanField(db_column="tut_ativo", default=False)

    class Meta:
        managed = False
        db_table = 'tutor'
    def __str__(self):
        return self.tut_nome

    def ativar(self):
        self.tut_ativo = True
        self.save()

    def desativar(self):
        self.tut_ativo = False
        self.save()

class Interprete(models.Model):
    int_id = models.AutoField(db_column='int_id', primary_key=True)
    int_nome = models.CharField(db_column='int_nome', max_length=255)
    int_cpf = models.CharField(db_column='int_cpf', max_length=11)
    int_genero = models.CharField(db_column='int_genero', max_length=1, choices=generos)
    int_email_pessoal = models.EmailField(db_column='int_email_pessoal', max_length=255)
    int_email_institucional = models.EmailField(db_column='int_email_institucional', max_length=255)
    int_telefone = models.CharField(db_column='int_telefone', max_length=255)
    int_ativo = models.BooleanField(db_column="int_ativo", default=True)

    class Meta:
        managed = False
        db_table = 'interprete'
    def __str__(self):
        return self.int_nome

    def ativar(self):
        self.int_ativo = True
        self.save()

    def desativar(self):
        self.int_ativo = False
        self.save()