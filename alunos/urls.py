from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.aluIndex, name='aluIndex'),
    path('acompanhantes/', views.acompanhantes, name='acompanhantes'),
    path('<int:aluno_id>', views.aluno, name='aluno'),
]