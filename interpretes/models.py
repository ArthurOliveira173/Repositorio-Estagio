from django.db import models

# Create your models here.

generos = (
    ('M', 'Masculino'),
    ('F', 'Feminino'),
)

class Interprete(models.Model):
    int_id = models.AutoField(db_column='int_id', primary_key=True)
    int_nome = models.CharField(db_column='int_nome', max_length=255)
    int_cpf = models.CharField(db_column='int_cpf', max_length=11)
    int_genero = models.CharField(db_column='int_genero', max_length=1, choices=generos)
    int_email_pessoal = models.EmailField(db_column='int_email_pessoal', max_length=255)
    int_email_institucional = models.EmailField(db_column='int_email_institucional', max_length=255)
    int_telefone = models.CharField(db_column='int_telefone', max_length=255)

    class Meta:
        managed = False
        db_table = 'interprete'
    def __str__(self):
        return self.int_nome