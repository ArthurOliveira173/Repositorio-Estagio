from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import validate_email
from string import ascii_letters
from django.contrib import messages
from membros.forms import AlunosForm

def authLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success('Login realizado com sucesso!')
            return redirect('aviIndex')
        else:
            messages.error(request, 'usuário ou senha inválidos!')
            return redirect('authLogin')
    else:
        return render(request, 'authenticate/authLogin.html', {

        })

def authLogout(request):
    logout(request)
    messages.success(request, "Você deslogou!")
    return redirect('authLogin')

def authRegister(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                messages.success(request, "Cadastrado com sucesso!")
                return redirect('authLogin')
            else:
                messages.error("Erro na tentativa de cadastro.")
                return redirect('authLogin')
    else:
        form = UserCreationForm()

    return render(request, 'authenticate/authRegister.html', {
        'form': form,
    })

def authRegisterAluno(request):
    if request.method == "POST":
        form = AlunosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            nome = request.POST.get('alu_nome')
            usuario = request.POST.get('alu_cpf')
            data_nascimento = request.POST.get('alu_data_nascimento')
            sexo = request.POST.get('alu_genero')
            email_pessoal = request.POST.get('alu_email_pessoal')
            email_instituicao = request.POST.get('alu_email_institucional')
            telefone = request.POST.get('alu_telefone')
            cep = request.POST.get('alu_endereco_cep')
            descricao_des = request.POST.get('alu_endereco_descricao')
            cidade = request.POST.get('alu_endereco_cidade')
            curso = request.POST.get(' alu_curso')
            periodo = request.POST.get('alu_periodo_academico')
            matricula = request.POST.get('alu_matricula')
            deficiencias = request.POST.get('alu_deficiencias')
            senha = request.POST.get('senha')
            senha2 = request.POST.get('senha2')

            if not nome or not usuario or not data_nascimento or not sexo or not email_pessoal or not email_instituicao or not telefone or not cep or not descricao_des or not cidade or not periodo or not matricula or not senha or not senha2:
                messages.error(request, 'Todos os campos devem ser preenchidos!')
                return render(request, 'authenticate/authRegisterAluno.html', {'form': form})

            try:
                valida_string(nome)
            except:
                messages.error(request, 'Por favor digite somente letras e espaços')
                return render(request, 'authenticate/authRegisterAluno.html', {'form': form})

            try:
                validate_email(email_pessoal)
            except:
                messages.error(request, 'Email pessoal invalido!')
                return render(request, 'authenticate/authRegisterAluno.html', {'form': form})

            try:
                validate_email(email_instituicao)
            except:
                messages.error(request, 'Email institucional invalido!')
                return render(request, 'authenticate/authRegisterAluno.html', {'form': form})

            try:
                valida_cpf(usuario)
            except:
                messages.error(request, 'O Cpf informado não é valido, tente novamente!')
                return render(request, 'authenticate/authRegisterAluno.html', {'form': form})

            if User.objects.filter(username=usuario).exists():
                messages.error(request, 'Cpf já cadastrado, verifique e tente novamente!')
                return render(request, 'authenticate/authRegisterAluno.html', {'form': form})

            if User.objects.filter(email=email_pessoal).exists():
                messages.error(request, 'Email pessoal já cadastrado, tente novamente!')
                return render(request, 'authenticate/authRegisterAluno.html', {'form': form})

            if User.objects.filter(email=email_instituicao).exists():
                messages.error(request, 'Email institucional já cadastrado, tente novamente!')
                return render(request, 'authenticate/authRegisterAluno.html', {'form': form})

            if len(senha) < 6:
                messages.error(request, 'Senha precisa ter 7 caracteres ou mais.')
                return render(request, 'authenticate/authRegisterAluno.html', {'form': form})

            if senha != senha2:
                messages.error(request, 'Senhas diferentes, tente novamente!')
                return render(request, 'authenticate/authRegisterAluno.html')

            user = User.objects.create_user(username=usuario, email=email_pessoal,
                                            password=senha, first_name=nome,
                                            last_name=email_instituicao)
            if user is not None:
                form.save()
                user.save()
                messages.success(request, 'Cadastro realizado com sucesso!')
                return redirect("authLogin")
            else:
                messages.error("ocorreu um erro na tentativa de cadastro! Usuário não foi criado.")
                return redirect("authLogin")
        else:
            messages.error(request, 'Informações invalidas, tente novamente!')
            form = AlunosForm(request.POST)
    else:
        form = AlunosForm()

    return render(request, 'authenticate/authRegisterAluno.html', {
        'form': form,
    })

def authRegisterMonitor(request):
    if request.method == "POST":
        form = AlunosForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                messages.success(request, "Cadastrado com sucesso!")
                return redirect('authLogin')
            else:
                messages.error("Erro na tentativa de cadastro.")
                return redirect('authLogin')
    else:
        form = AlunosForm()

    return render(request, 'authenticate/authRegister.html', {
        'form': form,
    })

def authRegisterTutor(request):
    if request.method == "POST":
        form = AlunosForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                messages.success(request, "Cadastrado com sucesso!")
                return redirect('authLogin')
            else:
                messages.error("Erro na tentativa de cadastro.")
                return redirect('authLogin')
    else:
        form = AlunosForm()

    return render(request, 'authenticate/authRegister.html', {
        'form': form,
    })

def authRegisterInterprete(request):
    if request.method == "POST":
        form = AlunosForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                messages.success(request, "Cadastrado com sucesso!")
                return redirect('authLogin')
            else:
                messages.error("Erro na tentativa de cadastro.")
                return redirect('authLogin')
    else:
        form = AlunosForm()

    return render(request, 'authenticate/authRegister.html', {
        'form': form,
    })

def valida_cpf(f):
    cpf = f
    novo_cpf = cpf[:-2]  # Elimina os dois últimos digitos do CPF
    reverso = 10  # Contador reverso
    total = 0

    # Loop do CPF
    for index in range(19):
        if index > 8:  # Primeiro índice vai de 0 a 9,
            index -= 9  # São os 9 primeiros digitos do CPF

        total += int(novo_cpf[index]) * reverso  # Valor total da multiplicação

        reverso -= 1  # Decrementa o contador reverso
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:  # Se o digito for > que 9 o valor é 0
                d = 0
            total = 0  # Zera o total
            novo_cpf += str(d)  # Concatena o digito gerado no novo cpf

    # Evita sequencias. Ex.: 11111111111, 00000000000...
    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

    # Descobri que sequências avaliavam como verdadeiro, então também
    # adicionei essa checagem aqui
    if cpf == novo_cpf and not sequencia:
        return True
    else:
        return False

def valida_string(s):
    validos = ascii_letters + ' áàâãéèêíïóôõöúçñ'
    while True:

        if all(c in validos for c in s):
            break  # sai do while
        else:
            return False