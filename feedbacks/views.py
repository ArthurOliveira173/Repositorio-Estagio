from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Feedbacks
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import FeedbacksForm, FeedbacksRespostaForm

from membros.models import AlunoPcd, CustomUser
from acompanhamentos.models import Acompanhamentos

# def handle_uploaded_file(f):
#     with open('avisos/uploads/'+f.name, 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)
def feeIndex(request):
    feedbacks = Feedbacks.objects.filter(fee_anterior=None)


    paginator = Paginator(feedbacks, 5)

    page = request.GET.get('p')
    feedbacks = paginator.get_page(page)

    feedbacks = reversed(feedbacks)
    return render(request, 'feedbacks/feeIndex.html', {
        'feedbacks': feedbacks
    })

def adicionarFeedback(request):
    submitted = False

    context = {}
    if request.POST:
        form = FeedbacksForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(request.FILES["avi_arquivos"])
            form.save()
            return HttpResponseRedirect('adicionarFeedback?submitted=True')
        else:
            form = FeedbacksForm()
            form.save()
            return HttpResponseRedirect('adicionarFeedback?submitted=True')
    else:
        form = FeedbacksForm()
        if 'submitted' in request.GET:
            submitted = True
    context['form'] = form
    context['submitted'] = submitted
    return render(request, 'feedbacks/adicionarFeedback.html', context)

def feedback(request, feedback_id):
    feedback = get_object_or_404(Feedbacks, fee_id=feedback_id)

    return render(request, 'feedbacks/feedback.html', {
        'feedback': feedback
    })

def atualizarFeedback(request, feedback_id):
    feedback = get_object_or_404(Feedbacks, fee_id=feedback_id)

    form = FeedbacksForm(request.POST or None, instance=feedback)
    if form.is_valid():
        form.save()
        return redirect('feeIndex')

    return render(request, 'feedbacks/atualizarFeedback.html', {
        'feedback': feedback,
        'form': form
    })

def buscarFeedback(request):
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            feedbacks = Feedbacks.objects.order_by('-fee_id').filter(Q(fee_titulo__icontains=searched) | Q(fee_descricao__icontains=searched) )
        else:
            feedbacks = None

        return render(request, 'feedbacks/buscarFeedback.html', {
            'searched': searched,
            'feedbacks': feedbacks
        })
    else:
        return render(request, 'feedbacks/buscarFeedback.html', {

        })



#ALUNO-FEEDBACK
def alunoFeedback(request, user_id):
    submitted = False
    context = {}

    if request.POST:
        form = FeedbacksForm(request.POST, request.FILES)
        user = get_object_or_404(CustomUser, id=user_id)
        aluno = get_object_or_404(AlunoPcd, alu_cpf= user.username)
        acompanhamento = Acompanhamentos.objects.filter(aco_aluno_pcd = aluno).last()

        if form.is_valid():
            Feedbackform = form.save(commit=False)
            # handle_uploaded_file(request.FILES["avi_arquivos"])
            Feedbackform.fee_acompanhamento = acompanhamento
            Feedbackform.save()
            return redirect('alunoFeedbackAll', user_id)
        else:
            form = FeedbacksForm()
            form.save()
            return HttpResponseRedirect('alunoFeedback?submitted=True')
    else:
        form = FeedbacksForm()
        if 'submitted' in request.GET:
            submitted = True
    context['form'] = form
    context['submitted'] = submitted

    return render (request, 'feedbacks/alunoFeedback.html', context)

def alunoFeedbackAll(request, user_id):

    user = get_object_or_404(CustomUser, id=user_id)
    aluno = get_object_or_404(AlunoPcd, alu_cpf=user.username)
    acompanhamento = Acompanhamentos.objects.filter(aco_aluno_pcd = aluno)
    feedback = Feedbacks.objects.filter(fee_acompanhamento__in=[a.aco_id for a in acompanhamento.all()], fee_anterior=None )

    paginator = Paginator(feedback, 7)
    page = request.GET.get('p')
    feedback = paginator.get_page(page)

    return render(request, 'feedbacks/alunofeedbackAll.html', {
        'feedback': feedback,
        'aluno': aluno,
        'acompanhamento': acompanhamento,
    })

def alunoOpenAllfeedback(request, user_id, feedback_id):

    user = get_object_or_404(CustomUser, id=user_id)
    aluno = get_object_or_404(AlunoPcd, alu_cpf=user.username)
    acompanhamento = Acompanhamentos.objects.filter(aco_aluno_pcd = aluno.alu_id)
    list_feedback = Feedbacks.objects.filter(fee_acompanhamento__in=[a.aco_id for a in acompanhamento.all()])

    feedback = []
    f0 = list_feedback[feedback_id - 1]
    feedback.append(f0)
    ultimo_feedback = None
    for f1 in list_feedback:
        if f1.fee_anterior == f0.fee_id:
            feedback.append(f1)
            f0=f1
        if f1.fee_proximo == None:
            ultimo_feedback = f1
    feedback = reversed(feedback)
    return render(request, 'feedbacks/alunoOpenAllfeedback.html', {
        'feedback': feedback,
        'aluno': aluno,
        'acompanhamento': acompanhamento,
        'ultimo_feedback': ultimo_feedback,
    })
def alunoOpenfeedback(request, user_id, feedback_id ):
    user = get_object_or_404(CustomUser, id=user_id)
    aluno = get_object_or_404(AlunoPcd, alu_cpf=user.username)
    feedback = get_object_or_404(Feedbacks, fee_id=feedback_id)
    acompanhamento = get_object_or_404(Acompanhamentos, aco_id = feedback.fee_acompanhamento.aco_id)

    if feedback.fee_proximo != None:
        return alunoOpenAllfeedback(request, user_id, feedback_id)
    return render(request, 'feedbacks/alunoOpenfeedback.html', {
        'feedback': feedback,
        'aluno': aluno,
        'acompanhamento': acompanhamento,
        'ultimo_feedback': feedback,

    })



'''https://django-portuguese.readthedocs.io/en/1.0/topics/forms/modelforms.html'''
def alunoRespostaFeedback(request, user_id, feedback_id):
    submitted = False
    context = {}
    user = get_object_or_404(CustomUser, id=user_id)
    aluno = get_object_or_404(AlunoPcd, alu_cpf=user.username)
    if request.POST:
        form = FeedbacksRespostaForm(request.POST, request.FILES)

        if form.is_valid():
            Feedbackform = form.save(commit=False)
            ultimo_feedback = get_object_or_404(Feedbacks, fee_id=feedback_id)

            Feedbackform.fee_anterior = ultimo_feedback.fee_id
            Feedbackform.fee_acompanhamento = ultimo_feedback.fee_acompanhamento


            Feedbackform.save()
            print(Feedbackform.fee_id)
            ultimo_feedback.fee_proximo = Feedbackform.fee_id
            ultimo_feedback.save()
            return redirect('alunoFeedbackAll', user_id)

        else:
            form = FeedbacksRespostaForm()
            form.save()
            return HttpResponseRedirect('alunoRespostaFeedback?submitted=True')
    else:
        form = FeedbacksRespostaForm()
        if 'submitted' in request.GET:
            submitted = True

    context['form'] = form
    context['submitted'] = submitted
    context['aluno'] = aluno

    return render(request, 'feedbacks/alunoRespostaFeedback.html', context)