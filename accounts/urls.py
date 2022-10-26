from django.urls import path, include
from . import views


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('cadastro/', views.cadastro, name='cadastro'),

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('cadastroAluno/', views.cadastroAluno, name='cadastroAluno'),
    path('cadastroMonitor', views.cadastroMonitor, name='cadastroMonitor'),
    path('cadastroTutor', views.cadastroTutor, name='cadastroTutor'),
    path('dashboardAluno/', views.dashboardAluno, name='dashboardAluno'),
]