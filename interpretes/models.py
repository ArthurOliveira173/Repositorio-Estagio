from django.db import models

# Create your models here.

class Interprete(models.Model):
    int_id = models.IntegerField(primary_key=True)
    int_nome = models.CharField(max_length=255)
    int_cpf = models.CharField(max_length=11)
    int_sexo = models.CharField(max_length=1)
    int_email = models.CharField(max_length=255)
    int_telefone = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'interprete'
    def __str__(self):
        return self.int_nome