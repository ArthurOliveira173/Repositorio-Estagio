from django import forms
from django.contrib.auth.models import User
from django.forms import ValidationError
from membros.models import AlunoPcd

class UserForm(forms.ModelForm):
    password = forms.CharField(required=True, widget=forms.PasswordInput(), label='Senha')

    def __init__(self, usuario=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.usuario=usuario

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')

    def clean(self, *args, **kwargs):
        data = self.data
        cleaned = self.cleaned_data



class AlunoForm(forms.ModelForm):
    class Meta:
        model = AlunoPcd
        fields = '__all__'
        exclude = ('alu_id', 'alu_user')


