from django.urls import path
from App_CS import views 

from django.contrib.auth.views import LogoutView



urlpatterns = [
    
    path("", views.inicio, name = "Inicio"),
    path("rodeos/", views.RodeoList.as_view(), name = "Rodeo"),
    path("rodeos/create", views.rodeoCreacion, name = "Create"),
    path("rodeos/detalle/<int:pk>/", views.RodeoDetalle.as_view(), name = "Rodeo_Ver"),
    path("rodeos/update/<int:id>/", views.editar_rodeo, name = "Rodeo_Update"),
    path("rodeos/delete/<int:pk>/", views.RodeoDelete.as_view(), name = "Rodeo_Delete"),

    path("shows/", views.ShowList.as_view(), name = "Show"),
    path("shows/create", views.showCreacion, name = "Create_Show"),
    path("shows/detalle/<int:pk>/", views.ShowDetalle.as_view(), name = "Show_Ver"),
    path("shows/update/<int:id>/", views.editar_show, name = "Show_Update"),
    path("shows/delete/<int:pk>/", views.ShowDelete.as_view(), name = "Show_Delete"),

    path("tickets/", views.ticket, name = "Ticket"),
    path("musics/", views.ticket, name = "Music"),

    path("about/", views.about, name = "About"),     
]

urlpatterns += [    
    path('login', views.login_request, name="Login"),
    path('registro', views.registro, name='Registro'),
    path('logout/', LogoutView.as_view(template_name='App_CS/logout.html'), name='Logout'),
    path('perfil_editar/', views.perfil_editar, name='Perfil_Editar'),
    
]
