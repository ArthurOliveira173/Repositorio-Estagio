# Generated by Django 4.1.1 on 2022-10-17 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('cur_id', models.AutoField(db_column='cur_id', primary_key=True, serialize=False)),
                ('cur_nome', models.CharField(db_column='cur_nome', max_length=255)),
                ('cur_quant_periodos', models.IntegerField(db_column='cur_quant_periodos')),
                ('cur_turno', models.CharField(choices=[('manha', 'Manha'), ('tarde', 'Tarde'), ('noite', 'Noite'), ('integral', 'Integral')], db_column='cur_turno', default='manha', max_length=8)),
            ],
            options={
                'db_table': 'cursos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Disciplinas',
            fields=[
                ('dis_id', models.AutoField(db_column='dis_id', primary_key=True, serialize=False)),
                ('dis_nome', models.CharField(db_column='dis_nome', max_length=255)),
            ],
            options={
                'db_table': 'disciplinas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Enderecos',
            fields=[
                ('end_id', models.AutoField(db_column='end_id', primary_key=True, serialize=False)),
                ('end_cep', models.CharField(db_column='end_cep', max_length=8)),
                ('end_descricao', models.CharField(db_column='end_descricao', max_length=255)),
                ('end_cidade', models.CharField(choices=[('RB', 'Rio Branco'), ('CS', 'Cruzeiro do Sul')], db_column='end_cidade', default='RB', max_length=100)),
            ],
            options={
                'db_table': 'enderecos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Laudos',
            fields=[
                ('lau_id', models.AutoField(db_column='lau_id', primary_key=True, serialize=False)),
                ('lau_status', models.CharField(choices=[('ativo', 'Ativo'), ('inativo', 'Inativo')], db_column='lau_status', default='ativo', max_length=255)),
                ('lau_numero', models.CharField(db_column='lau_numero', max_length=255)),
                ('lau_nome', models.CharField(db_column='lau_nome', max_length=255)),
                ('lau_arquivo', models.FileField(blank=True, db_column='lau_arquivo', null=True, upload_to='')),
            ],
            options={
                'db_table': 'laudos',
                'managed': False,
            },
        ),
    ]
