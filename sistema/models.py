from django.db import models

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