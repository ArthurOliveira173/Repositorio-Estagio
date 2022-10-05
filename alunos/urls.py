from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:aluno_id>', views.aluno, name='aluno'),
]