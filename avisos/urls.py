from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('adicionarAviso', views.adicionarAviso, name='adicionarAviso'),
    path('buscarAviso', views.buscarAviso, name='buscarAviso'),
    path('<int:aviso_id>', views.aviso, name='aviso'),

]