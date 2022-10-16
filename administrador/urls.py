from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.admIndex, name='admIndex'),
    path('homologar/', views.homologar, name='homologar'),
    path('alunos/', views.adminAlunos, name='alunos'),
    path('adicionarAluno', views.adicionarAluno, name='adicionarAluno'),
    path('buscarAluno', views.buscarAluno, name='buscarAluno'),
    path('<int:aluno_id>', views.admAluno, name='admAluno'),
    path('monitores/', views.adminMonitores, name='monitores'),
    path('tutores/', views.adminTutores, name='tutores'),
    path('interpretes/', views.adminInterpretes, name='interpretes')
]