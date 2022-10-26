# Generated by Django 4.1.2 on 2022-10-26 19:11

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
    ]
