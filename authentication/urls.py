from django.urls import path
from . import views

urlpatterns = [
    path('authLogin', views.authLogin, name='authLogin'),
    path('authLogout', views.authLogout, name='authLogout'),
    path('authRegister', views.authRegister, name='authRegister'),
    path('authRegisterGeral', views.authRegisterGeral, name='authRegisterGeral'),
    path('authRegisterAluno', views.authRegisterAluno, name='authRegisterAluno'),
    path('authRegisterMonitor', views.authRegisterMonitor, name='authRegisterMonitor'),
    path('authRegisterTutor', views.authRegisterTutor, name='authRegisterTutor'),
    path('authRegisterInterprete', views.authRegisterInterprete, name='authRegisterInterprete')
]