import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('cur_id', models.IntegerField(primary_key=True, serialize=False)),
                ('cur_descricao', models.CharField(max_length=255)),
                ('cur_quant_periodos', models.IntegerField()),
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
                ('dis_descricao', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'disciplinas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Avisos',
            fields=[
                ('avi_id', models.IntegerField(primary_key=True, serialize=False)),
                ('avi_titulo', models.CharField(max_length=255)),
                ('avi_descricao', models.CharField(blank=True, max_length=255, null=True)),
                ('avi_data', models.DateTimeField(default=django.utils.timezone.now)),
                ('avi_arquivos', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
