# Generated by Django 4.1.1 on 2022-10-17 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('mon_id', models.AutoField(db_column='mon_id', primary_key=True, serialize=False)),
                ('mon_nome', models.CharField(db_column='mon_nome', max_length=255)),
                ('mon_cpf', models.CharField(db_column='mon_cpf', max_length=11)),
                ('mon_genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], db_column='mon_genero', max_length=1)),
                ('mon_email_pessoal', models.EmailField(db_column='mon_email_pessoal', max_length=255)),
                ('mon_email_institucional', models.EmailField(db_column='mon_email_institucional', max_length=255)),
                ('mon_telefone', models.CharField(db_column='mon_telefone', max_length=255)),
                ('mon_matricula', models.CharField(db_column='mon_matricula', max_length=11)),
                ('mon_periodo_academico', models.CharField(db_column='mon_periodo_academico', max_length=255)),
            ],
            options={
                'db_table': 'monitor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('tut_id', models.AutoField(db_column='tut_id', primary_key=True, serialize=False)),
                ('tut_nome', models.CharField(db_column='tut_nome', max_length=255)),
                ('tut_cpf', models.CharField(db_column='tut_cpf', max_length=11)),
                ('tut_genero', models.CharField(db_column='tut_genero', max_length=1)),
                ('tut_email_pessoal', models.EmailField(db_column='tut_email_pessoal', max_length=255)),
                ('tut_email_institucional', models.EmailField(db_column='tut_email_institucional', max_length=255)),
                ('tut_telefone', models.CharField(db_column='tut_telefone', max_length=255)),
                ('tut_matricula', models.CharField(db_column='tut_matricula', max_length=11)),
                ('tut_periodo_academico', models.CharField(db_column='tut_periodo_academico', max_length=255)),
            ],
            options={
                'db_table': 'tutor',
                'managed': False,
            },
        ),
    ]
