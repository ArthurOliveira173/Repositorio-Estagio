from django import forms
from django.contrib.auth.models import User
from django.forms import ValidationError
from membros.models import AlunoPcd, Monitor, Tutor
from . uteis import valida_cpf

class AlunoForm(forms.ModelForm):
    class Meta:
        model = AlunoPcd
        fields = '__all__'
        exclude = ('alu_user', 'alu_nome', 'alu_cpf', 'alu_email_pessoal',
                   'alu_ativo',)

        labels = {
            'alu_genero': 'Sexo',
            'alu_email_institucional': 'E-mail institucional',
            'alu_telefone': 'Telefone(Celular)',
            'alu_endereco_cep': 'Cep',
            'alu_endereco_descricao': 'Endereço',
            'alu_endereco_cidade': 'Cidade',
            'alu_matricula': 'Número de Mátricula',
            'alu_deficiencias': 'Deficiencia',
            'alu_curso': 'Curso',
            'alu_periodo_academico': 'Período',
            'alu_data_nascimento': 'Data Nascimento',

        }

    def clean(self, *args, **kwargs):
        data = self.data
        cleaned = self.cleaned_data
        validation_error_msgs = {}
        
        email_institucional_data = cleaned.get('alu_email_institucional')
        telefone_data = cleaned.get('alu_telefone')
        cep_data = cleaned.get('alu_endereco_cep')
        endereco_descricao_data = cleaned.get('alu_endereco_descricao')
        cidade_data = cleaned.get('alu_endereco_cidade')
        matricula_data = cleaned.get('alu_matricula')
        deficiencias_data = cleaned.get('alu_deficiencias')
        curso_data = cleaned.get('alu_curso')
        periodo_data = cleaned.get('alu_periodo_academico')
        data_nascimento_data = cleaned.get('alu_data_nascimento')

        email_db = AlunoPcd.objects.filter(alu_email_institucional=email_institucional_data).first()

        error_msg_email_institucional_exists = 'E-mail institucional já existe'
        error_msg_required_field = 'Este campo é obrigatório'

        if not email_institucional_data:
            validation_error_msgs['alu_email_institucional'] = error_msg_required_field

        if not telefone_data:
            validation_error_msgs['alu_telefone'] = error_msg_required_field

        if not cep_data:
            validation_error_msgs['alu_endereco_cep'] = error_msg_required_field

        if not endereco_descricao_data:
            validation_error_msgs['alu_endereco_descricao'] = error_msg_required_field

        if not cidade_data:
            validation_error_msgs['alu_endereco_cidade'] = error_msg_required_field

        if not matricula_data:
            validation_error_msgs['alu_matricula'] = error_msg_required_field

        if not deficiencias_data:
            validation_error_msgs['alu_deficiencias'] = error_msg_required_field

        if not curso_data:
            validation_error_msgs['alu_curso'] = error_msg_required_field

        if not periodo_data:
            validation_error_msgs['alu_periodo_academico'] = error_msg_required_field

        if not data_nascimento_data:
            validation_error_msgs['alu_data_nascimento'] = error_msg_required_field

        if email_db:
            if email_institucional_data != email_db.alu_email_institucional:
               validation_error_msgs['alu_email_institucional'] = error_msg_email_institucional_exists
            
        if validation_error_msgs:
            raise(forms.ValidationError(validation_error_msgs))

class MonitorForm(forms.ModelForm):
    class Meta:
        model = Monitor
        fields = '__all__'
        exclude = ('mon_user', 'mon_nome', 'mon_cpf', 'mon_email_pessoal',
                   'mon_ativo',)

        labels = {
            'mon_genero': 'Sexo',
            'mon_email_institucional': 'E-mail institucional',
            'mon_telefone': 'Telefone(Celular)',
            'mon_endereco_cep': 'Cep',
            'mon_endereco_descricao': 'Endereço',
            'mon_endereco_cidade': 'Cidade Natal',
            'mon_matricula': 'Número de Mátricula',
            'mon_curso': 'Curso',
            'mon_periodo_academico': 'Período',
        }

    def clean(self, *args, **kwargs):
        data = self.data
        cleaned = self.cleaned_data
        validation_error_msgs = {}

        genero_data =cleaned.get('mon_genero')
        email_institucional_data = cleaned.get('mon_email_institucional')
        telefone_data = cleaned.get('mon_telefone')
        cep_data = cleaned.get('mon_endereco_cep')
        endereco_descricao_data = cleaned.get('mon_endereco_descricao')
        cidade_data = cleaned.get('mon_endereco_cidade')
        matricula_data = cleaned.get('mon_matricula')
        curso_data = cleaned.get('mon_curso')
        periodo_data = cleaned.get('mon_periodo_academico')
#        data_nascimento_data = cleaned.get('mon_data_nascimento')

        email_db = Monitor.objects.filter(mon_email_institucional=email_institucional_data).first()

        error_msg_email_institucional_exists = 'E-mail institucional já existe'
        error_msg_required_field = 'Este campo é obrigatório'

        if not genero_data:
            validation_error_msgs['mon_genero'] = error_msg_required_field


        if not email_institucional_data:
            validation_error_msgs['mon_email_institucional'] = error_msg_required_field

        if not telefone_data:
            validation_error_msgs['mon_telefone'] = error_msg_required_field

        if not cep_data:
            validation_error_msgs['mon_endereco_cep'] = error_msg_required_field

        if not endereco_descricao_data:
            validation_error_msgs['mon_endereco_descricao'] = error_msg_required_field

        if not cidade_data:
            validation_error_msgs['mon_endereco_cidade'] = error_msg_required_field

        if not matricula_data:
            validation_error_msgs['mon_matricula'] = error_msg_required_field

        if not curso_data:
            validation_error_msgs['mon_curso'] = error_msg_required_field

        if not periodo_data:
            validation_error_msgs['mon_periodo_academico'] = error_msg_required_field

#        if not data_nascimento_data:
#            validation_error_msgs['mon_data_nascimento'] = error_msg_required_field

        if email_db:
            if email_institucional_data != email_db.alu_email_institucional:
                validation_error_msgs['mon_email_institucional'] = error_msg_email_institucional_exists

        if validation_error_msgs:
            raise (forms.ValidationError(validation_error_msgs))

class TutorForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = '__all__'
        exclude = ('tut_user', 'tut_nome', 'tut_cpf', 'tut_email_pessoal',
                   'tut_ativo',)

        labels = {
            'tut_genero': 'Sexo',
            'tut_email_institucional': 'E-mail institucional',
            'tut_telefone': 'Telefone(Celular)',
            'tut_endereco_cep': 'Cep',
            'tut_endereco_descricao': 'Endereço',
            'tut_endereco_cidade': 'Cidade Natal',
            'tut_matricula': 'Número de Mátricula',
            'tut_curso': 'Curso',
            'tut_periodo_academico': 'Período',
            'tut_data_nascimento': 'Data Nascimento',

        }

    def clean(self, *args, **kwargs):
        data = self.data
        cleaned = self.cleaned_data
        validation_error_msgs = {}

        genero_data =cleaned.get('tut_genero')
        email_institucional_data = cleaned.get('tut_email_institucional')
        telefone_data = cleaned.get('tut_telefone')
        cep_data = cleaned.get('tut_endereco_cep')
        endereco_descricao_data = cleaned.get('tut_endereco_descricao')
        cidade_data = cleaned.get('tut_endereco_cidade')
        matricula_data = cleaned.get('tut_matricula')
        curso_data = cleaned.get('tut_curso')
        periodo_data = cleaned.get('tut_periodo_academico')
#        data_nascimento_data = cleaned.get('mon_data_nascimento')

        email_db = Tutor.objects.filter(tut_email_institucional=email_institucional_data).first()

        error_msg_email_institucional_exists = 'E-mail institucional já existe'
        error_msg_required_field = 'Este campo é obrigatório'

        if not genero_data:
            validation_error_msgs['tut_genero'] = error_msg_required_field


        if not email_institucional_data:
            validation_error_msgs['tut_email_institucional'] = error_msg_required_field

        if not telefone_data:
            validation_error_msgs['tut_telefone'] = error_msg_required_field

        if not cep_data:
            validation_error_msgs['tut_endereco_cep'] = error_msg_required_field

        if not endereco_descricao_data:
            validation_error_msgs['tut_endereco_descricao'] = error_msg_required_field

        if not cidade_data:
            validation_error_msgs['tut_endereco_cidade'] = error_msg_required_field

        if not matricula_data:
            validation_error_msgs['tut_matricula'] = error_msg_required_field

        if not curso_data:
            validation_error_msgs['tut_curso'] = error_msg_required_field

        if not periodo_data:
            validation_error_msgs['tut_periodo_academico'] = error_msg_required_field

#        if not data_nascimento_data:
#            validation_error_msgs['mon_data_nascimento'] = error_msg_required_field

        if email_db:
            if email_institucional_data != email_db.tut_email_institucional:
                validation_error_msgs['tut_email_institucional'] = error_msg_email_institucional_exists

        if validation_error_msgs:
            raise (forms.ValidationError(validation_error_msgs))

class UserForm(forms.ModelForm):
    password = forms.CharField(required=False, widget=forms.PasswordInput(), label='Senha')
    password2 = forms.CharField(required=False, widget=forms.PasswordInput(), label='Confirmação de Senha')

    def __init__(self, usuario=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.usuario= usuario

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'password2')

        labels = {
            'first_name': 'Primeiro nome',
            'last_name': 'Segundo nome',
            'username': 'CPF',
            'email': 'Digite seu e-mail',
        }


    def clean(self, *args, **kwargs):
        data = self.data
        cleaned = self.cleaned_data
        validation_error_msgs = {}


        usuario_data = cleaned.get('username')
        password_data = cleaned.get('password')
        password2_data = cleaned.get('password2')
        email_data = cleaned.get('email')

        usuario_db = User.objects.filter(username=usuario_data).first()
        email_db = User.objects.filter(email=email_data).first()

        error_msg_user_exists = 'CPF já existe'
        error_msg_password_match = 'Senhas não conferem'
        error_msg_password_short = 'Senha precisa ter pelo menos 6 caracteres'
        error_msg_email_exists = 'E-mail já existe'
        error_msg_required_field = 'Este campo é obrigatório'
        error_msg_invalid_cpf = 'Digite um CPF válido'

        if not valida_cpf(usuario_data):
            validation_error_msgs['username'] = error_msg_invalid_cpf
        #se o usuário estiver logado
        if self.usuario:
            if usuario_db:
                if usuario_data != usuario_db.username:
                    validation_error_msgs['username'] = error_msg_user_exists

            if email_db:
                if email_data != email_db.email:
                    validation_error_msgs['email'] = error_msg_email_exists

            if password_data:
                if len(password_data) < 6:
                    validation_error_msgs['password'] = error_msg_password_short

                if password_data != password2_data:
                    validation_error_msgs['password'] = error_msg_password_match
                    validation_error_msgs['password2'] = error_msg_password_match



        #usuário não logado
        else:
            if usuario_db:
                validation_error_msgs['username'] = error_msg_user_exists

            if email_db:
                validation_error_msgs['email'] = error_msg_email_exists

            if not password_data:
                validation_error_msgs['password'] = error_msg_required_field

            if not password2_data:
                validation_error_msgs['password2'] = error_msg_required_field

            if len(password_data) < 6:
                validation_error_msgs['password'] = error_msg_password_short

            if password_data != password2_data:
                validation_error_msgs['password'] = error_msg_password_match
                validation_error_msgs['password2'] = error_msg_password_match

        if validation_error_msgs:
            raise(forms.ValidationError(validation_error_msgs))
