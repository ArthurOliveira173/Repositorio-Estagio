# Generated by Django 4.1.2 on 2022-12-02 14:09

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
                ('fee_titulo', models.CharField(db_column='fee_titulo', max_length=255)),
                ('fee_descricao', models.TextField(blank=True, db_column='fee_descricao', max_length=255, null=True)),
                ('fee_data', models.DateTimeField(db_column='fee_data', default=django.utils.timezone.now)),
                ('fee_arquivo', models.FileField(blank=True, db_column='fee_arquivo', null=True, upload_to='')),
            ],
            options={
                'db_table': 'feedbacks',
                'managed': False,
            },
        ),
    ]
