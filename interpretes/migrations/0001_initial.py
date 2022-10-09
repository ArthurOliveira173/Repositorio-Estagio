# Generated by Django 2.2.3 on 2022-10-09 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interprete',
            fields=[
                ('int_id', models.IntegerField(db_column='int_id', primary_key=True, serialize=False)),
                ('int_nome', models.CharField(db_column='int_nome', max_length=255)),
                ('int_cpf', models.CharField(db_column='int_cpf', max_length=11)),
                ('int_sexo', models.CharField(db_column='int_sexo', max_length=1)),
                ('int_email', models.CharField(db_column='int_email', max_length=255)),
                ('int_telefone', models.CharField(db_column='int_telefone', max_length=255)),
            ],
            options={
                'db_table': 'interprete',
                'managed': False,
            },
        ),
    ]
