from django import forms
from django.contrib.auth.models import User
from django.forms import ValidationError
from membros.models import AlunoPcd

class UserForm(forms.ModelForm):
    password = forms.CharField(required=True, widget=forms.PasswordInput(), label='Senha')
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(), label='Confirmação de Senha')

    def __init__(self, usuario=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.usuario=usuario

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'password2')

    def clean(self, *args, **kwargs):
        data = self.data
        cleaned = self.cleaned_data
        validation_error_msgs = {}

        usuario_data = cleaned.get('username')
        password_data = cleaned.get('password')
        password2_data = cleaned.get('password2')
        email_data = cleaned.get('email')

        usuario_db = User.objects.filter(username=usuario_data).first()
        email_db = User.objects.filter(email=usuario_data).first()

        error_msg_user_exists = 'Usuário já existe'
        error_msg_password_match = 'Senhas não conferem'
        error_msg_password_short = 'A senha precisa ter pelo menos 6 caracteres'
        error_msg_email_exists = 'Email já existe'


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

        else:
            validation_error_msgs['username'] = 'erro no usuário'

        if validation_error_msgs:
            raise(forms.ValidationError(validation_error_msgs))

class AlunoForm(forms.ModelForm):
    class Meta:
        model = AlunoPcd
        fields = '__all__'
        exclude = ('alu_id', 'alu_user')


