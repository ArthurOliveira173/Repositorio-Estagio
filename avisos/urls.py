from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.aviIndex, name='aviIndex'),
    path('adicionarAviso', views.adicionarAviso, name='adicionarAviso'),
    path('buscarAviso', views.buscarAviso, name='buscarAviso'),
    path('aviso/<int:aviso_id>', views.aviso, name='aviso'),
    path('atualizarAviso/<int:aviso_id>', views.atualizarAviso, name='atualizarAviso'),
    path('deletarAviso/<int:aviso_id>', views.deletarAviso, name='deletarAviso'),

]