from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_administrador= models.BooleanField(default=False)
    is_aluno = models.BooleanField(default=False)
    is_interprete = models.BooleanField(default=False)
    is_monitor = models.BooleanField(default=False)
    is_tutor = models.BooleanField(default=False)