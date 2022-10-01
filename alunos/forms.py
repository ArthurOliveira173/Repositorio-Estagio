from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django import forms
from .models import AlunoPcd


class AlunoForms(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = AlunoPcd

    @transaction.atomic
    def data_save(self):
        user = super().save(commit=False)
        AlunoPcd.alu_nome = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.is_student = True
        user.save()
        student = AlunoPcd.objects.create(user=user)
        student.class_name = self.cleaned_data.get('class_name')
        student.phone_number = self.cleaned_data.get('phone_number')
        student.save()
        return user