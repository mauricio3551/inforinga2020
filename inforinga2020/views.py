from django.shortcuts import render

def Home(request):
    return render(request,'index.html')

def Login(request):
    return render(request,'usuarios/login.html')

def CrearPost(request):
    return render(request,'crearPost.html')

def PosteosRecientes(request):
    return render(request,'PosteosRecientes.html')

def ComentariosRecientes(request):
    return render(request,'ComentariosRecientes.html')