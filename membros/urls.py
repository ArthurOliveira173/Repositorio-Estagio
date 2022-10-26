from django.urls import path, include
from . import views
urlpatterns = [
    #Admin
    path('admin/', views.admIndex, name='admIndex'),
    path('admin/homologar', views.homologar, name='homologar'),
    path('admin/alunos/', views.adminAlunos, name='alunos'),
    path('admin/adicionarAluno', views.adicionarAluno, name='adicionarAluno'),
    path('admin/buscarAluno', views.buscarAluno, name='buscarAluno'),
    path('admin/alunos/<int:aluno_id>', views.admAluno, name='admAluno'),
    path('admin/atualizarAluno/<int:aluno_id>', views.atualizarAluno, name='atualizarAluno'),
    path('admin/deletarAluno/<int:aluno_id>', views.deletarAluno, name='deletarAluno'),
    path('admin/monitores/', views.adminMonitores, name='monitores'),
    path('admin/adicionarMonitor', views.adicionarMonitor, name='adicionarMonitor'),
    path('admin/buscarMonitor', views.buscarMonitor, name='buscarMonitor'),
    path('admin/monitores/<int:monitor_id>', views.admMonitor, name='admMonitor'),
    path('admin/atualizarMonitor/<int:monitor_id>', views.atualizarMonitor, name='atualizarMonitor'),
    path('admin/deletarMonitor/<int:monitor_id>', views.deletarMonitor, name='deletarMonitor'),
    path('admin/tutores/', views.adminTutores, name='tutores'),
    path('admin/adicionarTutor', views.adicionarTutor, name='adicionarTutor'),
    path('admin/buscarTutor', views.buscarTutor, name='buscarTutor'),
    path('admin/tutores/<int:tutor_id>', views.admTutor, name='admTutor'),
    path('admin/atualizarTutor/<int:tutor_id>', views.atualizarTutor, name='atualizarTutor'),
    path('admin/deletarTutor/<int:tutor_id>', views.deletarTutor, name='deletarTutor'),
    path('admin/interpretes/', views.adminInterpretes, name='interpretes'),
    path('admin/adicionarInterprete', views.adicionarInterprete, name='adicionarInterprete'),
    path('admin/buscarInterprete', views.buscarInterprete, name='buscarInterprete'),
    path('admin/interpretes/<int:interprete_id>', views.admInterprete, name='admInterprete'),
    path('admin/atualizarInterprete/<int:interprete_id>', views.atualizarInterprete, name='atualizarInterprete'),
    path('admin/deletarInterprete/<int:interprete_id>', views.deletarInterprete, name='deletarInterprete'),

    #Alunos
    path('alunos', views.aluIndex, name='aluIndex'),
    path('alunos/acompanhantes', views.acompanhantes, name='acompanhantes'),
    path('alunos/<int:aluno_id>', views.aluno, name='aluno'),
    #Monitor_tutor
    path('monitores', views.index_mon, name='index_mon'),
    path('monitores/monAluno', views.monAluno, name='monAluno'),
    path('monitores/monitor/<int:monitor_id>', views.monitor, name='monitor'),
    path('tutores', views.index_tut, name='index_tut'),
    path('tutores/tutAluno', views.tutAluno, name='tutAluno'),
    path('tutores/tutor/<int:tutor_id>', views.tutor, name='tutor'),
    #Interpretes
    path('interpretes', views.intIndex, name='intIndex'),
    path('interpretes/intAluno', views.intAluno, name='intAluno'),
    path('interpretes/<int:interprete_id>', views.interprete, name='interprete')
]