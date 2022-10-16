from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.acoIndex, name='acoIndex'),
    path('adicionarAcompanhamento', views.adicionarAcompanhamento, name='adicionarAcompanhamento'),
    path('buscarAcompanhamento', views.buscarAcompanhamento, name='buscarAcompanhamento'),
    path('acompanhamento/<int:acompanhamento_id>', views.acompanhamento, name='acompanhamento'),
    path('atualizarAcompanhamento/<int:acompanhamento_id>', views.atualizarAcompanhamento, name='atualizarAcompanhamento'),

]