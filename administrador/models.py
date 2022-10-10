from django.db import models

# Create your models here.
class Administrador(models.Model):
    adm_id = models.AutoField(db_column='adm_id', primary_key=True, )
    adm_nome = models.CharField(db_column='adm_nome', max_length=255)
    adm_cpf = models.CharField(db_column='adm_cpf', max_length=11)
    adm_email = models.EmailField(db_column='adm_email', max_length=255)

    class Meta:
        managed = False
        db_table = 'administrador'
    def __str__(self):
        return self.adm_nome