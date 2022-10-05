from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:interprete_id>', views.interprete, name='interprete')
]