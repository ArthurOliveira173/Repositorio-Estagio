# Generated by Django 4.1.7 on 2023-03-01 19:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RelatoriosMon',
            fields=[
                ('relM_id', models.AutoField(db_column='relM_id', primary_key=True, serialize=False)),
                ('relM_titulo', models.CharField(db_column='relM_titulo', max_length=255)),
                ('relM_data', models.DateTimeField(db_column='relM_data', default=django.utils.timezone.now)),
                ('relM_arquivo', models.FileField(blank=True, db_column='relM_arquivo', null=True, upload_to='')),
            ],
            options={
                'db_table': 'relatorios_monitoria',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RelatoriosTut',
            fields=[
                ('relT_id', models.AutoField(db_column='relT_id', primary_key=True, serialize=False)),
                ('relT_titulo', models.CharField(db_column='relT_titulo', max_length=255)),
                ('relT_data', models.DateTimeField(db_column='relT_data', default=django.utils.timezone.now)),
                ('relT_arquivo', models.FileField(blank=True, db_column='relT_arquivo', null=True, upload_to='')),
            ],
            options={
                'db_table': 'relatorios_tutoria',
                'managed': False,
            },
        ),
    ]
