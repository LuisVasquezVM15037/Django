#crear mi rutas
from django.urls import path
from . import views

urlpatterns = [
    #inicio es el nombre de la ruta
    path('',views.inicio, name='inicio'),
    path('nosotros',views.nosotros, name='nosotros'),
]



