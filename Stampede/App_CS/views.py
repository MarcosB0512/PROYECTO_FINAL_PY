from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from django.core.files.storage import default_storage
from django.conf import settings
from PIL import Image

from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import Avatar, Rodeo, Imagen, Show, Imagen_Show
from .forms  import FormularioRodeo, EditarUsuarioForm, EditarRodeoForm, FormularioShow, EditarShowForm
import os
from django.contrib.auth import login as django_login, logout, authenticate
from .forms  import UserRegistroForm
from django.contrib.auth.models import User


def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, "App_CS/inicio.html")

def about(request):
    return render(request, "App_CS/about.html")

def ticket(request):
    return render(request, "App_CS/tickets.html")

class RodeoList(ListView):
    model = Rodeo
    template_name = "App_CS/rodeos.html"

class RodeoDetalle(DetailView):
    model = Rodeo
    template_name = "App_CS/rodeo_ver.html"

class ShowList(ListView):
    model = Show
    template_name = "App_CS/shows.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        shows = context['object_list']

        imagen_shows = Imagen_Show.objects.filter(show__in=shows)
        context['imagen_shows'] = imagen_shows

        return context


class ShowDetalle(DetailView):
    model = Show
    template_name = "App_CS/show_ver.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        show = self.object 

        imagen_shows = Imagen_Show.objects.filter(show=show)
        context['imagen_shows'] = imagen_shows
        return context

def registro(request):

    if request.method == "POST":
        form = UserRegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "App_CS/login.html", {"form": form})
        else:
            return render(request, "App_CS/login.html", {"form": form})
    
    else:
        form = UserRegistroForm()
        return render(request, "App_CS/registro.html", {"form": form})
   

def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=contraseña)

            if user is not None:
                django_login(request, user)
                return render(request,"App_CS/inicio.html", {"mensaje":usuario})
            else:
                return render(request, "App_CS/login.html", {"mensaje": "Datos Incorrecto"})
        else:
            return render(request, "App_CS/login.html", {"formulario": form})
        
    form = AuthenticationForm()
    return render(request, "App_CS/login.html", {"formulario": form})


@login_required
def perfil_editar(request):
    usuario = request.user
    user = User.objects.get(username=request.user)
    print(user)
           
    if request.method == "POST":
        formulario = EditarUsuarioForm(request.POST, request.FILES)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario.email = informacion['email']
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']
            usuario.save()

            user = User.objects.get(username=request.user)
            print(user)
            
            avatar = Avatar.objects.filter(user=user).first()
            print(avatar)

            if not avatar:
                avatar = Avatar(user=user)

            nombre_avatar = formulario.cleaned_data['avatar'].name
            ruta_avatar = os.path.join('avatares', nombre_avatar)

            if os.path.join('avatares', nombre_avatar):
                avatar.imagen.name = ruta_avatar
            else:
                avatar.imagen = formulario.cleaned_data['avatar']
                avatar.imagen.name = ruta_avatar

            avatar.save()
            return render(request, 'App_CS/inicio.html')
        else:
            formulario = EditarUsuarioForm()

    else: 
        formulario = EditarUsuarioForm(initial={
                'email': usuario.email,
                'first_name':usuario.first_name,
                'last_name':usuario.last_name
            }
        )

    return render(request, "App_CS/perfil_editar.html",
        {
            "formulario": formulario,
            "usuario": usuario
        }
    )


@login_required
def rodeoCreacion(request):
     
    if request.method == "POST":

        form = FormularioRodeo(request.POST, request.FILES)
        if form.is_valid():
           rodeo = form.save(commit=False)
           rodeo.user_id = request.user.id
           form.save()
           
           imagen = form.cleaned_data['imagen']
           Imagen.objects.create(user=request.user, rodeo=rodeo, imagen=imagen)
           
           return render(request, "App_CS/rodeos.html", {"form": form})
        
        else:
           
           return render(request, "App_CS/rodeos.html", {"form": form})
    
    else:   
        
        form = FormularioRodeo()
        return render(request, "App_CS/rodeos.html", {"form": form})

def editar_rodeo(request, id):
    usuario = request.user
    user = User.objects.get(username=request.user)
    rodeo = Rodeo.objects.get(id=id)

    imagen_actual = Imagen.objects.filter(rodeo=rodeo).first()

    if request.method == "POST":
        formulario = EditarRodeoForm(request.POST, request.FILES)
        rodeo = Rodeo.objects.get(id=id)

        if formulario.is_valid():

            informacion = formulario.cleaned_data
            rodeo.titulo = informacion['titulo']
            rodeo.descripcion = informacion['descripcion']
            rodeo.texto = informacion['texto']
            rodeo.save()

            imagen_actual = Imagen.objects.filter(rodeo=rodeo).first()
            nueva_imagen = formulario.cleaned_data['imagen']

            if nueva_imagen:
                if imagen_actual:
                    default_storage.delete(settings.MEDIA_ROOT + '/' + str(imagen_actual.imagen))
                    imagen_actual.delete()
                Imagen.objects.create(user=user, rodeo=rodeo, imagen=nueva_imagen)
        
            return redirect('Rodeo')
        
        else:
            formulario = EditarRodeoForm(initial={
                'titulo': rodeo.titulo,
                'descripcion': rodeo.descripcion,
                'texto': rodeo.texto,
            })

            imagen_actual = Imagen.objects.filter(rodeo=rodeo).first()

            return render(request, "App_CS/rodeo_form.html", {
                "formulario": formulario,
                "usuario": usuario,
                "imagen_actual": imagen_actual,
                "titulo": rodeo.titulo,
                'descripcion': rodeo.descripcion,
                'texto': rodeo.texto,
            })

    else:
        formulario = EditarRodeoForm(initial={
        'titulo': rodeo.titulo,
        'descripcion': rodeo.descripcion,
        'texto': rodeo.texto,
    })

        imagen_actual = Imagen.objects.filter(rodeo=rodeo).first()

        return render(request, "App_CS/rodeo_form.html", {
            "formulario": formulario,
            "usuario": usuario,
            "imagen_actual": imagen_actual,
            "titulo": rodeo.titulo,
            'descripcion': rodeo.descripcion,
            'texto': rodeo.texto,
        })
    

class RodeoDelete(DeleteView):
    model = Rodeo
    template_name = "App_CS/rodeo_confirm_delete.html"
    success_url = reverse_lazy('Rodeo')
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    

@login_required
def showCreacion(request):
     
    if request.method == "POST":
        form = FormularioShow(request.POST, request.FILES)
        if form.is_valid():
           show = form.save(commit=False)
           show.user_id = request.user.id
           form.save()
           
           imagen = form.cleaned_data['imagen']
           Imagen_Show.objects.create(user=request.user, show=show, imagen=imagen)
           
           return redirect('Show')
        
        else:
           return redirect('Show')
           
    
    else:
        form = FormularioShow()
        return render(request, "App_CS/shows.html", {"form": form})

def editar_show(request, id):
    usuario = request.user
    user = User.objects.get(username=request.user)
    show = Show.objects.get(id=id)

    imagen_actual = Imagen_Show.objects.filter(show=show).first()

    if request.method == "POST":
        formulario = EditarShowForm(request.POST, request.FILES)
        show = Show.objects.get(id=id)

        if formulario.is_valid():

            informacion = formulario.cleaned_data
            show.titulo = informacion['titulo']
            show.descripcion = informacion['descripcion']
            show.texto = informacion['texto']
            show.save()

            imagen_actual = Imagen_Show.objects.filter(show=show).first()
            nueva_imagen = formulario.cleaned_data['imagen']

            if nueva_imagen:
                if imagen_actual:
                    default_storage.delete(settings.MEDIA_ROOT + '/' + str(imagen_actual.imagen))
                    imagen_actual.delete()
                Imagen_Show.objects.create(user=user, show=show, imagen=nueva_imagen)
        
            return redirect('Show')
        
        else:
            formulario = EditarShowForm(initial={
                'titulo': show.titulo,
                'descripcion': show.descripcion,
                'texto': show.texto,
            })

            imagen_actual = Imagen_Show.objects.filter(show=show).first()

            return render(request, "App_CS/show_form.html", {
                "formulario": formulario,
                "usuario": usuario,
                "imagen_actual": imagen_actual,
                "titulo": show.titulo,
                'descripcion': show.descripcion,
                'texto': show.texto,
            })

    else:
        formulario = EditarShowForm(initial={
        'titulo': show.titulo,
        'descripcion': show.descripcion,
        'texto': show.texto,
    })

        imagen_actual = Imagen_Show.objects.filter(show=show).first()

        return render(request, "App_CS/show_form.html", {
            "formulario": formulario,
            "usuario": usuario,
            "imagen_actual": imagen_actual,
            "titulo": show.titulo,
            'descripcion': show.descripcion,
            'texto': show.texto,
        })
    

class ShowDelete(DeleteView):
    model = Show
    template_name = "App_CS/show_confirm_delete.html"
    success_url = reverse_lazy('Show')
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    
    
