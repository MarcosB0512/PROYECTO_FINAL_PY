from django.db import models
from django.contrib.auth.models import User

class Rodeo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=40)
    descripcion = models.TextField(max_length=450)
    texto = models.TextField()
    fecha_create = models.DateTimeField(auto_created=True, null=True)
    fecha_update = models.DateTimeField(auto_now=True, null=True)

    @property
    def date(self):
        return self.user.first_name

    def __str__(self):
        return f"Nombre: {self.user}, Fecha_Creacion: {self.fecha_create}"
    
class Show(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=40)
    descripcion = models.TextField(max_length=450)
    texto = models.TextField()
    fecha_create = models.DateTimeField(auto_created=True, null=True)
    fecha_update = models.DateTimeField(auto_now=True, null=True)

    @property
    def date(self):
        return self.user.first_name

    def __str__(self):
        return f"Nombre: {self.user}, Fecha_Creacion: {self.fecha_create}"

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.FileField(upload_to='avatares', null=True, blank=True)

    @property
    def date(self):
        return self.user.first_name
    
    def __str__(self):
        return f"{self.user} - {self.imagen}"
    
    
class Imagen(models.Model):
    imagen = models.ImageField(upload_to='imagenes/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rodeo = models.OneToOneField(Rodeo, on_delete=models.CASCADE, primary_key=True)
    
    @property
    def date(self):
        return self.user.first_name
    
    def __str__(self):
        return f"{self.user} - {self.imagen}"
    
class Imagen_Show(models.Model):
    imagen = models.ImageField(upload_to='imagenes/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    show = models.OneToOneField(Show, on_delete=models.CASCADE, primary_key=True)

    @property
    def date(self):
        return self.user.first_name
    
    def __str__(self):
        return f"{self.user} - {self.imagen}"