from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('homologar/', views.homologar, name='homologar'),
    path('alunos/', views.adminAlunos, name='alunos'),
    path('monitorTutor/', views.adminMonitorTutor, name='monitorTutor'),
    path('interpretes/', views.adminInterpretes, name='interpretes')
]