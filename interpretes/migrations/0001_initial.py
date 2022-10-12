# Generated by Django 4.1.1 on 2022-10-12 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interprete',
            fields=[
                ('int_id', models.AutoField(db_column='int_id', primary_key=True, serialize=False)),
                ('int_nome', models.CharField(db_column='int_nome', max_length=255)),
                ('int_cpf', models.CharField(db_column='int_cpf', max_length=11)),
                ('int_genero', models.CharField(db_column='int_genero', max_length=1)),
                ('int_email', models.EmailField(db_column='int_email', max_length=255)),
                ('int_telefone', models.CharField(db_column='int_telefone', max_length=255)),
            ],
            options={
                'db_table': 'interprete',
                'managed': False,
            },
        ),
    ]
