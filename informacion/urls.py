#crear mi rutas
from django.urls import path
from . import views

urlpatterns = [
    #inicio es el nombre de la ruta
    #nombre es de la funcion creada en vista
    path('',views.inicio, name='inicio'),
    path('nosotros',views.nosotros, name='nosotros'),
    path('blogs',views.blogs, name='blogs'),
]



