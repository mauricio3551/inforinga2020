from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.Home , name='inicio'),    
    path('CrearPost' , views.CrearPost , name='crearPost'), 
    path('PosteosRecientes' , views.PosteosRecientes , name='PosteosRecientes'), 
    path('ComentariosRecientes' , views.ComentariosRecientes , name='ComentariosRecientes'),
    path('Login' , auth.LoginView.as_view(template_name="usuarios/login.html") , name='login'),
    path('Logout' , auth.LogoutView.as_view() , name='logout'),

    #URL INCLUIDAS

    path('Usuarios',include('apps.usuarios.urls'))
]
