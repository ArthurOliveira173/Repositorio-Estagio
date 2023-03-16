from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avisos',
            fields=[
                ('avi_id', models.AutoField(db_column='avi_id', primary_key=True, serialize=False)),
                ('avi_titulo', models.CharField(db_column='avi_titulo', max_length=255)),
                ('avi_descricao', models.TextField(blank=True, db_column='avi_descricao', max_length=255, null=True)),
                ('avi_data', models.DateTimeField(db_column='avi_data', default=django.utils.timezone.now)),
                ('avi_arquivos', models.FileField(blank=True, db_column='avi_arquivos', null=True, upload_to='')),
                ('avi_mostrar', models.BooleanField(db_column='avi_mostrar', default=True)),
            ],
            options={
                'db_table': 'avisos',
                'managed': False,
            },
        ),
    ]
