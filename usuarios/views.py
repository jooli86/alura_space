from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User

def login(request):
    form = LoginForms()

    if request.method == "POST":
        form = CadastroForms(request.POST)

    return render(request, "usuarios/login.html", {"form": form})

def cadastro(request):
    form = CadastroForms()

    if request.method == "POST":
        form = CadastroForms(request.POST)


        if form.is_valid():

            if form["senha_1"].value() != form["senha_2"].value():
                return redirect("cadastro")

            nome = form.cleaned_data.get("nome_cadastro")
            email = form.cleaned_data.get("email")
            senha = form.cleaned_data.get("senha_1")

            if User.objects.filter(username=nome).exists():
                return redirect("cadastro")
            
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            return redirect("login")
            
    return render(request, "usuarios/cadastro.html", {"form": form})
