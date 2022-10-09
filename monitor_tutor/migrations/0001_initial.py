# Generated by Django 4.1.1 on 2022-10-09 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('mon_id', models.IntegerField(db_column='mon_id', primary_key=True, serialize=False)),
                ('mon_nome', models.CharField(db_column='mon_nome', max_length=255)),
                ('mon_cpf', models.CharField(db_column='mon_cpf', max_length=11)),
                ('mon_sexo', models.CharField(db_column='mon_sexo', max_length=1)),
                ('mon_email', models.CharField(db_column='mon_email', max_length=255)),
                ('mon_telefone', models.CharField(db_column='mon_telefone', max_length=255)),
                ('mon_matricula', models.CharField(db_column='mon_matricula', max_length=11)),
                ('mon_periodo_academico', models.CharField(db_column='mon_periodo_academico', max_length=255)),
                ('mon_tipo', models.CharField(db_column='mon_tipo', max_length=7)),
            ],
            options={
                'db_table': 'monitor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('tut_id', models.IntegerField(db_column='tut_id', primary_key=True, serialize=False)),
                ('tut_nome', models.CharField(db_column='tut_nome', max_length=255)),
                ('tut_cpf', models.CharField(db_column='tut_cpf', max_length=11)),
                ('tut_sexo', models.CharField(db_column='tut_sexo', max_length=1)),
                ('tut_email', models.CharField(db_column='tut_email', max_length=255)),
                ('tut_telefone', models.CharField(db_column='tut_telefone', max_length=255)),
                ('tut_matricula', models.CharField(db_column='tut_matricula', max_length=11)),
                ('tut_periodo_academico', models.CharField(db_column='tut_periodo_academico', max_length=255)),
                ('tut_tipo', models.CharField(db_column='tut_tipo', max_length=7)),
            ],
            options={
                'db_table': 'tutor',
                'managed': False,
            },
        ),
    ]
