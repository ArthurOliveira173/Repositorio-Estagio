from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('404', views.erro404, name='erro404'),
]