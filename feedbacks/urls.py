from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.feeIndex, name='feeIndex'),
    path('adicionarFeedback', views.adicionarFeedback, name='adicionarFeedback'),
    path('buscarFeedback', views.buscarFeedback, name='buscarFeedback'),
    path('feedback/<int:feedback_id>', views.feedback, name='feedback'),
    path('atualizarFeedback/<int:feedback_id>', views.atualizarFeedback, name='atualizarFeedback'),

    #ALUNO
    path('feedback/alunoFeedback/<int:user_id>', views.alunoFeedback, name='alunoFeedback'),
    path('feedback/alunoFeedbackAll/<int:user_id>', views.alunoFeedbackAll, name='alunoFeedbackAll'),
    path('feedback/alunoFeedbackAll/<int:user_id>/alunoOpenfeedback/<int:feedback_id>', views.alunoOpenfeedback, name='alunoOpenfeedback'),
    path('feedback/alunoFeedbackAll/<int:user_id>/alunoOpenAllfeedback/<int:feedback_id>', views.alunoOpenAllfeedback, name='alunoOpenAllfeedback'),
    path('feedback/alunoRespostaFeedback/<int:user_id>/<int:feedback_id>/', views.alunoRespostaFeedback, name='alunoRespostaFeedback'),

]