from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('homologar/', views.homologar, name='homologar'),
    path('alunos/', views.adminAlunos, name='alunos'),
    path('adicionarAluno', views.adicionarAluno, name='adicionarAluno'),
    path('buscarAluno', views.buscarAluno, name='buscarAluno'),
    path('<int:aluno_id>', views.aluno, name='aluno'),
    path('monitorTutor/', views.adminMonitorTutor, name='monitorTutor'),
    path('interpretes/', views.adminInterpretes, name='interpretes')
]