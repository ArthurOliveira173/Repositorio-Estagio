from django.urls import path
from . import views


urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('login/', views.loginUsuario, name='login'),
    path('logout/', views.logoutUsuario, name='logout'),
    path('index/', views.index, name='index'),
    path('registroAluno/', views.RegistroAluno.as_view(), name='registroAluno'),
    path('registroAdministrador/', views.RegistroAdministrador.as_view(), name='registroAdministrador'),
    path('registroMonitor/', views.RegistroMonitor.as_view(), name='registroMonitor'),
    path('registroTutor/', views.RegistroTutor.as_view(), name='registroTutor'),
    path('registroInterprete/', views.RegistroInterprete.as_view(), name='registroInterprete'),
]