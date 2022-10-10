# Generated by Django 4.1.1 on 2022-10-10 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlunoPcd',
            fields=[
                ('alu_id', models.AutoField(db_column='alu_id', primary_key=True, serialize=False)),
                ('alu_nome', models.CharField(db_column='alu_nome', max_length=255)),
                ('alu_cpf', models.CharField(db_column='alu_cpf', max_length=11)),
                ('alu_sexo', models.CharField(db_column='alu_sexo', max_length=1)),
                ('alu_email', models.EmailField(db_column='alu_email', max_length=255)),
                ('alu_telefone', models.CharField(db_column='alu_telefone', max_length=255)),
                ('alu_matricula', models.CharField(db_column='alu_matricula', max_length=11)),
                ('alu_deficiencias', models.CharField(blank=True, db_column='alu_deficiencias', max_length=255, null=True)),
                ('alu_periodo_academico', models.CharField(db_column='alu_Periodo_Academico', max_length=255)),
                ('alu_data_nascimento', models.DateField(db_column='alu_data_nascimento')),
            ],
            options={
                'db_table': 'aluno_pcd',
                'managed': False,
            },
        ),
    ]
