from django.db import models

# Create your models here.

class Interprete(models.Model):
    int_id = models.AutoField(db_column='int_id', primary_key=True)
    int_nome = models.CharField(db_column='int_nome', max_length=255)
    int_cpf = models.CharField(db_column='int_cpf', max_length=11)
    int_genero = models.CharField(db_column='int_genero', max_length=1)
    int_email = models.EmailField(db_column='int_email', max_length=255)
    int_telefone = models.CharField(db_column='int_telefone', max_length=255)

    class Meta:
        managed = False
        db_table = 'interprete'
    def __str__(self):
        return self.int_nome