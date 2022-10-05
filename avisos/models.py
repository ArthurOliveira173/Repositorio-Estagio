from django.db import models
from django.utils import timezone


class Avisos(models.Model):
    avi_id = models.IntegerField(primary_key=True)
    avi_titulo = models.CharField(max_length=255)
    avi_descricao = models.CharField(max_length=255, blank=True, null=True)
    avi_data = models.DateTimeField(default = timezone.now)
    avi_arquivos = models.TextField(blank=True, null=True)
    avi_mostrar = models.BooleanField(default=True)
    def __str__(self):
        return self.avi_titulo