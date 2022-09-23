from django.db import models
class Avisos(models.Model):
    avi_id = models.IntegerField(primary_key=True)
    avi_titulo = models.CharField(max_length=255)
    avi_descricao = models.CharField(max_length=255, blank=True, null=True)
    avi_data = models.DateTimeField()
    avi_arquivos = models.TextField(blank=True, null=True)