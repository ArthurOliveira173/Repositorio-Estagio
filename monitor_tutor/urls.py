from django.urls import path, include
from . import views
urlpatterns = [
    path('monitor', views.index_mon, name='index_mon'),
    path('monitor/<int:monitor_id>', views.monitor, name='monitor'),
    path('tutor', views.index_tut, name='index_tut'),
    path('tutor/<int:tutor_id>', views.tutor, name='tutor'),

]
