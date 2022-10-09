# Generated by Django 4.1.1 on 2022-10-09 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('cur_id', models.IntegerField(db_column='cur_id', primary_key=True, serialize=False)),
                ('cur_nome', models.CharField(db_column='cur_nome', max_length=255)),
                ('cur_quant_periodos', models.IntegerField(db_column='cur_quant_periodos')),
                ('cur_horario', models.CharField(choices=[('Manha', 'Manha'), ('Tarde', 'Tarde'), ('Noite', 'Noite'), ('Integral', 'Integral')], db_column='cur_horario', default='Manha', max_length=8)),
            ],
            options={
                'db_table': 'cursos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Disciplinas',
            fields=[
                ('dis_id', models.IntegerField(primary_key=True, serialize=False)),
                ('dis_nome', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'disciplinas',
                'managed': False,
            },
        ),
    ]
