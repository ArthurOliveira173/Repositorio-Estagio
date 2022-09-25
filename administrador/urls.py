from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('homologacao/', views.homologar, name='homologar')
]