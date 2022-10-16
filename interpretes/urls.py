from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.intIndex, name='intIndex'),
    path('intAluno/', views.intAluno, name='intAluno'),
    path('<int:interprete_id>', views.interprete, name='interprete')
]