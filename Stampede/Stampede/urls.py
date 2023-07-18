#from django.contrib import admin
#from django.urls import path
#from .views import Inicio

#urlpatterns = [
#    path("admin/", admin.site.urls),
#    path("", Inicio)
#]

#########

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("App_CS.urls")),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


