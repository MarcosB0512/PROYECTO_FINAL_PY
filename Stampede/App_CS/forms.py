from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import datetime
from .models import Rodeo, Avatar, Imagen, Show

class UserRegistroForm(UserCreationForm):
    email = forms.EmailField(label='Correo')
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class AvatarForm(forms.Form):
    avatar: forms.FileField()

class EditarUsuarioForm(forms.Form):
    email = forms.EmailField(label="Ingrese su Email:")
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    avatar = forms.FileField()

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'avatar']

class FormularioRodeo(forms.ModelForm):
    titulo = forms.CharField(widget=forms.TextInput(), required=True, error_messages={
        'required': 'Por favor, introduce un título.',
    })
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'class': 'custom-textarea'}), required=True, error_messages={
        'required': 'Por favor, introduce un título.',
    })

    texto = forms.CharField(widget=forms.Textarea(attrs={'class': 'custom-textarea'}), required=True, error_messages={
        'required': 'Por favor, introduce un texto.',
    })

    imagen = forms.ImageField(required=True, error_messages={
        'required': 'Por favor, selecciona una imagen.',
    })

    class Meta:
        model = Rodeo
        fields = ['titulo', 'descripcion', 'texto', 'imagen']

class EditarRodeoForm(forms.ModelForm):
    titulo = forms.CharField(widget=forms.TextInput())
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'class': 'custom-textarea'}))
    texto = forms.TextInput()
    imagen = forms.ImageField(required=False)

    class Meta:
        model = Rodeo
        fields = ['titulo', 'descripcion', 'texto', 'imagen']

class ImagenForm(forms.Form):
    imagen = forms.ImageField()

class FormularioShow(forms.ModelForm):
    titulo = forms.CharField(widget=forms.TextInput())
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'class': 'custom-textarea'}))
    texto = forms.CharField(widget=forms.Textarea(attrs={'class': 'custom-textarea'}))
    imagen = forms.ImageField()

    class Meta:
        model = Show
        fields = ['titulo', 'descripcion', 'texto', 'imagen']

class EditarShowForm(forms.ModelForm):
    titulo = forms.CharField(widget=forms.TextInput())
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'class': 'custom-textarea'}))
    texto = forms.TextInput()
    imagen = forms.ImageField(required=False)

    class Meta:
        model = Show
        fields = ['titulo', 'descripcion', 'texto', 'imagen']
