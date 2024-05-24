#crear mi rutas
from django.urls import path
from . import views
from .views import exit

urlpatterns = [
    #inicio es el nombre de la ruta
    #nombre es de la funcion creada en vista
    path('',views.inicio, name='inicio'),
    path('inicio2',views.inicio2, name='inicio2'),
    #aqui van las demas 2023,2022,2021,2020
    path('tra2023',views.tra2023, name='tra2023'),
    path('tra2022',views.tra2022, name='tra2022'),
    path('tra2021',views.tra2021, name='tra2021'),
    path('tra2020',views.tra2020, name='tra2020'),
    
    

    path('nosotros',views.nosotros, name='nosotros'),
    path('blogs',views.blogs, name='blogs'),
    path('crear_blogs',views.crear_blogs, name='crear'),
    path('editar',views.editar, name='editar'),
    path('logout/',exit, name='exit'),

   
]



