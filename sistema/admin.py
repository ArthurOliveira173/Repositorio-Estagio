from django.contrib import admin
from .models import Cursos, Disciplinas, Enderecos, Laudos
# Register your models here.

admin.site.register(Cursos)
admin.site.register(Disciplinas)
admin.site.register(Enderecos)
admin.site.register(Laudos)