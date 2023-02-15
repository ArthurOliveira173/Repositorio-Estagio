# Generated by Django 4.1.1 on 2023-02-15 15:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcompanhamentoDisciplinas',
            fields=[
                ('AsDis_id', models.AutoField(db_column='AsDis_id', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'acompanhamento_disciplina',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AcompanhamentoInterpretes',
            fields=[
                ('AsInt_id', models.AutoField(db_column='AsInt_id', primary_key=True, serialize=False)),
                ('AsInt_inicio', models.DateField(db_column='AsInt_inicio', default=django.utils.timezone.now)),
                ('AsInt_fim', models.DateField(db_column='AsInt_fim', default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'acompanhamento_interprete',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AcompanhamentoMonitores',
            fields=[
                ('AsMon_id', models.AutoField(db_column='AsMon_id', primary_key=True, serialize=False)),
                ('AsMon_inicio', models.DateField(db_column='AsMon_inicio', default=django.utils.timezone.now)),
                ('AsMon_fim', models.DateField(db_column='AsMon_fim', default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'acompanhamento_monitoria',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Acompanhamentos',
            fields=[
                ('aco_id', models.AutoField(db_column='aco_id', primary_key=True, serialize=False)),
                ('aco_semestre', models.CharField(db_column='aco_semestre', max_length=6)),
                ('aco_inicio', models.DateField(db_column='aco_inicio', default=django.utils.timezone.now)),
                ('aco_fim', models.DateField(db_column='aco_fim', default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'acompanhamento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AcompanhamentoTutores',
            fields=[
                ('AsTut_id', models.AutoField(db_column='AsTut_id', primary_key=True, serialize=False)),
                ('AsTut_inicio', models.DateField(db_column='AsTut_inicio', default=django.utils.timezone.now)),
                ('AsTut_fim', models.DateField(db_column='AsTut_fim', default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'acompanhamento_tutoria',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HorariosDisciplina',
            fields=[
                ('HoDis_id', models.AutoField(db_column='HoDis_id', primary_key=True, serialize=False)),
                ('HoDis_dia', models.CharField(choices=[('Segunda-feira', 'Segunda-feira'), ('Terça-feira', 'Terça-feira'), ('Quarta-feira', 'Quarta-feira'), ('Quinta-feira', 'Quinta-feira'), ('Sexta-feira', 'Sexta-feira'), ('Sábado', 'Sábado')], db_column='HoDis_dia', max_length=255)),
                ('HoDis_inicio', models.TimeField(db_column='HoDis_inicio', default=django.utils.timezone.now)),
                ('HoDis_fim', models.TimeField(db_column='HoDis_Fim', default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'horarios_disciplina',
                'managed': False,
            },
        ),
    ]
