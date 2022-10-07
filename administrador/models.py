from django.db import models

# Create your models here.
class Administrador(models.Model):
    adm_id = models.IntegerField(primary_key=True)
    adm_nome = models.CharField(max_length=255)
    adm_cpf = models.CharField(max_length=11)
    adm_email = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'administrador'
    def __str__(self):
        return self.adm_nome