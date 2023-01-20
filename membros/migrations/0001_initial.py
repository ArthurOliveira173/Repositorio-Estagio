# Generated by Django 4.1.1 on 2023-01-20 20:48

import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('adm_id', models.AutoField(db_column='adm_id', primary_key=True, serialize=False)),
                ('adm_nome', models.CharField(db_column='adm_nome', max_length=255)),
                ('adm_cpf', models.CharField(db_column='adm_cpf', max_length=11)),
                ('adm_email', models.EmailField(db_column='adm_email', max_length=255)),
                ('permissao', models.IntegerField(choices=[(0, 'Admin'), (1, 'Aluno'), (2, 'Monitor'), (3, 'Tutor'), (4, 'Interprete')], db_column='permissao', default=0)),
            ],
            options={
                'db_table': 'administrador',
                'managed': False,
            },
        ),
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
                ('alu_endereco_cep', models.CharField(db_column='alu_endereco_cep', max_length=255)),
                ('alu_endereco_descricao', models.CharField(db_column='alu_endereco_descricao', max_length=255)),
                ('alu_endereco_cidade', models.CharField(choices=[('RB', 'Rio Branco'), ('CS', 'Cruzeiro do Sul')], db_column='alu_endereco_cidade', max_length=255)),
                ('alu_matricula', models.CharField(db_column='alu_matricula', max_length=11)),
                ('alu_deficiencias', models.CharField(blank=True, db_column='alu_deficiencias', max_length=255, null=True)),
                ('alu_periodo_academico', models.CharField(db_column='alu_periodo_academico', max_length=255)),
                ('alu_data_nascimento', models.DateField(db_column='alu_data_nascimento')),
                ('alu_ativo', models.BooleanField(db_column='alu_ativo', default=False)),
                ('permissao', models.IntegerField(choices=[(0, 'Admin'), (1, 'Aluno'), (2, 'Monitor'), (3, 'Tutor'), (4, 'Interprete')], db_column='permissao', default=1)),
            ],
            options={
                'db_table': 'aluno_pcd',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Interprete',
            fields=[
                ('int_id', models.AutoField(db_column='int_id', primary_key=True, serialize=False)),
                ('int_nome', models.CharField(db_column='int_nome', max_length=255)),
                ('int_cpf', models.CharField(db_column='int_cpf', max_length=11)),
                ('int_genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], db_column='int_genero', max_length=1)),
                ('int_email_pessoal', models.EmailField(db_column='int_email_pessoal', max_length=255)),
                ('int_email_institucional', models.EmailField(db_column='int_email_institucional', max_length=255)),
                ('int_telefone', models.CharField(db_column='int_telefone', max_length=255)),
                ('int_ativo', models.BooleanField(db_column='int_ativo', default=True)),
                ('permissao', models.IntegerField(choices=[(0, 'Admin'), (1, 'Aluno'), (2, 'Monitor'), (3, 'Tutor'), (4, 'Interprete')], db_column='permissao', default=4)),
            ],
            options={
                'db_table': 'interprete',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('mon_id', models.AutoField(db_column='mon_id', primary_key=True, serialize=False)),
                ('mon_nome', models.CharField(db_column='mon_nome', max_length=255)),
                ('mon_cpf', models.CharField(db_column='mon_cpf', max_length=11)),
                ('mon_genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], db_column='mon_genero', max_length=1)),
                ('mon_email_pessoal', models.EmailField(db_column='mon_email_pessoal', max_length=255)),
                ('mon_email_institucional', models.EmailField(db_column='mon_email_institucional', max_length=255)),
                ('mon_telefone', models.CharField(db_column='mon_telefone', max_length=255)),
                ('mon_endereco_cep', models.CharField(db_column='mon_endereco_cep', max_length=255)),
                ('mon_endereco_descricao', models.CharField(db_column='mon_endereco_descricao', max_length=255)),
                ('mon_endereco_cidade', models.CharField(choices=[('RB', 'Rio Branco'), ('CS', 'Cruzeiro do Sul')], db_column='mon_endereco_cidade', max_length=255)),
                ('mon_matricula', models.CharField(db_column='mon_matricula', max_length=11)),
                ('mon_periodo_academico', models.CharField(db_column='mon_periodo_academico', max_length=255)),
                ('mon_ativo', models.BooleanField(db_column='mon_ativo', default=False)),
                ('permissao', models.IntegerField(choices=[(0, 'Admin'), (1, 'Aluno'), (2, 'Monitor'), (3, 'Tutor'), (4, 'Interprete')], db_column='permissao', default=2)),
            ],
            options={
                'db_table': 'monitor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('tut_id', models.AutoField(db_column='tut_id', primary_key=True, serialize=False)),
                ('tut_nome', models.CharField(db_column='tut_nome', max_length=255)),
                ('tut_cpf', models.CharField(db_column='tut_cpf', max_length=11)),
                ('tut_genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], db_column='tut_genero', max_length=1)),
                ('tut_email_pessoal', models.EmailField(db_column='tut_email_pessoal', max_length=255)),
                ('tut_email_institucional', models.EmailField(db_column='tut_email_institucional', max_length=255)),
                ('tut_telefone', models.CharField(db_column='tut_telefone', max_length=255)),
                ('tut_endereco_cep', models.CharField(db_column='tut_endereco_cep', max_length=255)),
                ('tut_endereco_descricao', models.CharField(db_column='tut_endereco_descricao', max_length=255)),
                ('tut_endereco_cidade', models.CharField(choices=[('RB', 'Rio Branco'), ('CS', 'Cruzeiro do Sul')], db_column='tut_endereco_cidade', max_length=255)),
                ('tut_matricula', models.CharField(db_column='tut_matricula', max_length=11)),
                ('tut_periodo_academico', models.CharField(db_column='tut_periodo_academico', max_length=255)),
                ('tut_ativo', models.BooleanField(db_column='tut_ativo', default=False)),
                ('permissao', models.IntegerField(choices=[(0, 'Admin'), (1, 'Aluno'), (2, 'Monitor'), (3, 'Tutor'), (4, 'Interprete')], db_column='permissao', default=3)),
            ],
            options={
                'db_table': 'tutor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.PositiveSmallIntegerField(choices=[(0, 'Admin'), (1, 'Aluno'), (2, 'Monitor'), (3, 'Tutor'), (4, 'Interprete')])),
                ('is_active', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
    ]
