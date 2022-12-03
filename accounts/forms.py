from django import forms
from django.contrib.auth.models import User
from django.forms import ValidationError
from membros.models import AlunoPcd
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
            validation_error_msgs['alu_email_institucional'] = error_msg_email_institucional_exists
            
        if validation_error_msgs:
            raise(forms.ValidationError(validation_error_msgs))


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