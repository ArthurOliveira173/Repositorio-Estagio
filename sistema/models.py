from django.db import models
from django.utils import timezone

Cidades = (
    ('RB', 'Rio Branco'),
    ('CS', 'Cruzeiro do Sul'),
)
Turnos = (
    ('manha', 'Manha'),
    ('tarde', 'Tarde'),
    ('noite', 'Noite'),
    ('integral', 'Integral'),
)
LaudoStatus = (
    ('ativo', 'Ativo'),
    ('inativo', 'Inativo'),
)

class Enderecos(models.Model):

    end_id = models.AutoField(db_column='end_id', primary_key=True)
    end_cep = models.CharField(db_column='end_cep', max_length=8)
    end_descricao = models.CharField(db_column='end_descricao', max_length=255)
    end_cidade = models.CharField(db_column='end_cidade', max_length=100, choices=Cidades, default='RB')

    class Meta:
        managed = False
        db_table = 'enderecos'

    def __str__(self):
        return "{0}, {1}".format(self.end_descricao, self.end_cidade)

class Cursos(models.Model):

    cur_id = models.AutoField(db_column='cur_id', primary_key=True)
    cur_nome = models.CharField(db_column="cur_nome", max_length=255)
    cur_quant_periodos = models.IntegerField(db_column="cur_quant_periodos")
    cur_turno = models.CharField(db_column="cur_turno", max_length=8, choices=Turnos, default='manha')

    class Meta:
        managed = False
        db_table = 'cursos'

    def __str__(self):
        return self.cur_nome

class Disciplinas(models.Model):

    dis_id = models.AutoField(db_column='dis_id', primary_key=True)
    dis_nome = models.CharField(max_length=255)
    dis_cur = models.ForeignKey(Cursos, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disciplinas'
    def __str__(self):
        return self.dis_nome

class Laudos(models.Model):

    lau_id = models.AutoField(db_column='lau_id', primary_key=True)
    lau_status = models.CharField(db_column='lau_status', max_length=255, choices=LaudoStatus, default='ativo')
    lau_numero = models.CharField(db_column='lau_numero', max_length=255)
    lau_nome = models.CharField(db_column='lau_nome', max_length=255)
    lau_arquivo = models.FileField(db_column='lau_arquivo', blank=True, null=True)
    lau_aluno = models.ForeignKey('alunos.AlunoPcd', on_delete=models.DO_NOTHING, db_column='lau_aluno', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'laudos'

    def __str__(self):
        return "{0}: {1}".format(self.lau_numero, self.lau_nome)