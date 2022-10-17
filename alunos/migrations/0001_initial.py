# Generated by Django 4.1.1 on 2022-10-17 01:18

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
                ('alu_genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], db_column='alu_genero', max_length=1)),
                ('alu_email_pessoal', models.EmailField(db_column='alu_email_pessoal', max_length=255)),
                ('alu_email_institucional', models.EmailField(db_column='alu_email_institucional', max_length=255)),
                ('alu_telefone', models.CharField(db_column='alu_telefone', max_length=255)),
                ('alu_matricula', models.CharField(db_column='alu_matricula', max_length=11)),
                ('alu_deficiencias', models.CharField(blank=True, db_column='alu_deficiencias', max_length=255, null=True)),
                ('alu_periodo_academico', models.CharField(db_column='alu_periodo_academico', max_length=255)),
                ('alu_data_nascimento', models.DateField(db_column='alu_data_nascimento')),
            ],
            options={
                'db_table': 'aluno_pcd',
                'managed': False,
            },
        ),
    ]
