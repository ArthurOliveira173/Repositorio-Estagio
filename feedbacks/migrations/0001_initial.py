# Generated by Django 4.1.7 on 2023-03-14 14:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedbacks',
            fields=[
                ('fee_id', models.AutoField(db_column='fee_id', primary_key=True, serialize=False)),
                ('fee_titulo', models.CharField(choices=[('Prefiro não Falar', 'Prefiro não Falar'), ('Construtivo', 'Construtivo'), ('Negativo', 'Negativo'), ('Positivo', 'Positivo'), ('Ocorrência ofensiva', 'Ocorrência ofensiva')], db_column='fee_titulo', default='Prefiro não Falar', max_length=255)),
                ('fee_descricao', models.TextField(blank=True, db_column='fee_descricao', max_length=255, null=True)),
                ('fee_data', models.DateTimeField(db_column='fee_data', default=django.utils.timezone.now)),
                ('fee_arquivo', models.FileField(blank=True, db_column='fee_arquivo', null=True, upload_to='')),
                ('fee_anterior', models.IntegerField(blank=True, db_column='fee_anterior')),
                ('fee_proximo', models.IntegerField(blank=True, db_column='fee_proximo')),
            ],
            options={
                'db_table': 'feedbacks',
                'managed': False,
            },
        ),
    ]
