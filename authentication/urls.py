from django.urls import path
from . import views

urlpatterns = [
    path('authLogin', views.authLogin, name='authLogin'),
    path('authLogout', views.authLogout, name='authLogout'),
]