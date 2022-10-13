from django.urls import path, include
from . import views
urlpatterns = [
    path('monitores', views.index_mon, name='index_mon'),
    path('monAluno', views.monAluno, name='monAluno'),
    path('monitor/<int:monitor_id>', views.monitor, name='monitor'),
    path('tutores', views.index_tut, name='index_tut'),
    path('tutAluno', views.tutAluno, name='tutAluno'),
    path('tutor/<int:tutor_id>', views.tutor, name='tutor'),

]
