from django.db import models
from django.utils import timezone

class Cursos(models.Model):

    class Turno(models.TextChoices):
        MANHA = "Manha"
        Tarde = "Tarde"
        NOITE = "Noite"
        INTEGRAL = "Integral"

    cur_id = models.IntegerField(db_column="cur_id", primary_key=True)
    cur_nome = models.CharField(db_column="cur_nome", max_length=255)
    cur_quant_periodos = models.IntegerField(db_column="cur_quant_periodos")
    cur_horario = models.CharField(db_column="cur_horario", max_length=8, choices=Turno.choices, default=Turno.MANHA)

    class Meta:
        managed = False
        db_table = 'cursos'

    def __str__(self):
        return self.cur_nome

class Disciplinas(models.Model):
    dis_id = models.IntegerField(primary_key=True)
    dis_nome = models.CharField(max_length=255)
    dis_cur = models.ForeignKey(Cursos, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disciplinas'
    def __str__(self):
        return self.dis_nome