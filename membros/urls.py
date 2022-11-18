from django.urls import path, include
from . import views
urlpatterns = [
    #Admin
    path('admin/', views.admIndex, name='admIndex'),
    path('admin/homologarAtivo', views.homologarAtivo, name='homologarAtivo'),
    path('admin/homologarInativo', views.homologarInativo, name='homologarInativo'),
    path('admin/homologarAlunoAtivo/<int:aluno_id>', views.homologarAlunoAtivo, name='homologarAlunoAtivo'),
    path('admin/homologarAlunoInativo/<int:aluno_id>', views.homologarAlunoInativo, name='homologarAlunoInativo'),
    path('admin/homologarInterpreteAtivo<int:interprete_id>', views.homologarInterpreteAtivo, name='homologarInterpreteAtivo'),
    path('admin/homologarInterpreteInativo<int:interprete_id>', views.homologarInterpreteInativo, name='homologarInterpreteInativo'),
    path('admin/homologarMonitorAtivo/<int:monitor_id>', views.homologarMonitorAtivo, name='homologarMonitorAtivo'),
    path('admin/homologarMonitorInativo/<int:monitor_id>', views.homologarMonitorInativo, name='homologarMonitorInativo'),
    path('admin/homologarTutorAtivo/<int:tutor_id>', views.homologarTutorAtivo, name='homologarTutorAtivo'),
    path('admin/homologarTutorInativo/<int:tutor_id>', views.homologarTutorInativo, name='homologarTutorInativo'),
    path('admin/buscarAtivo', views.buscarAtivo, name='buscarAtivo'),
    path('admin/buscarInativo', views.buscarInativo, name='buscarInativo'),
    path('admin/ativarAluno/<int:aluno_id>', views.ativarAluno, name='ativarAluno'),
    path('admin/ativarMonitor/<int:monitor_id>', views.ativarMonitor, name='ativarMonitor'),
    path('admin/ativarTutor/<int:tutor_id>', views.ativarTutor, name='ativarTutor'),
    path('admin/ativarInterprete/<int:interprete_id>', views.ativarInterprete, name='ativarInterprete'),
    path('admin/desativarAluno/<int:aluno_id>', views.desativarAluno, name='desativarAluno'),
    path('admin/desativarMonitor/<int:monitor_id>', views.desativarMonitor, name='desativarMonitor'),
    path('admin/desativarTutor/<int:tutor_id>', views.desativarTutor, name='desativarTutor'),
    path('admin/desativarInterprete/<int:interprete_id>', views.desativarInterprete, name='desativarInterprete'),
    path('admin/deletarAlunoAtivo/<int:aluno_id>', views.deletarAlunoAtivo, name='deletarAlunoAtivo'),
    path('admin/deletarAlunoInativo/<int:aluno_id>', views.deletarAlunoInativo, name='deletarAlunoInativo'),
    path('admin/deletarMonitorAtivo/<int:monitor_id>', views.deletarMonitorAtivo, name='deletarMonitorAtivo'),
    path('admin/deletarMonitorInativo/<int:monitor_id>', views.deletarMonitorInativo, name='deletarMonitorInativo'),
    path('admin/deletarTutorAtivo/<int:tutor_id>', views.deletarTutorAtivo, name='deletarTutorAtivo'),
    path('admin/deletarTutorInativo/<int:tutor_id>', views.deletarTutorInativo, name='deletarTutorInativo'),
    path('admin/deletarInterpreteAtivo/<int:interprete_id>', views.deletarInterpreteAtivo, name='deletarInterpreteAtivo'),
    path('admin/deletarInterpreteInativo/<int:interprete_id>', views.deletarInterpreteInativo, name='deletarInterpreteInativo'),
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
    path('usuarioIndex', views.usuarioIndex, name='usuarioIndex'),
    path('alunos/perfilAluno', views.perfilAluno, name='perfilAluno'),

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