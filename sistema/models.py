from django.db import models
from django.utils import timezone

class Cursos(models.Model):
    cur_id = models.IntegerField(primary_key=True)
    cur_descricao = models.CharField(max_length=255)
    cur_quant_periodos = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cursos'

    def __str__(self):
        return self.cur_descricao

class Disciplinas(models.Model):
    dis_id = models.IntegerField(primary_key=True)
    dis_descricao = models.CharField(max_length=255)
    dis_cur = models.ForeignKey(Cursos, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disciplinas'
    def __str__(self):
        return self.dis_descricao

class Avisos(models.Model):
    avi_id = models.IntegerField(primary_key=True)
    avi_titulo = models.CharField(max_length=255)
    avi_descricao = models.CharField(max_length=255, blank=True, null=True)
    avi_data = models.DateTimeField(default = timezone.now)
    avi_arquivos = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.avi_titulo