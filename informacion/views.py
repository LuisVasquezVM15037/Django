from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request, 'paginaweb/inicio.html')

def inicio2(request):
    return render(request, 'paginaweb/inicio2.html')


def nosotros(request):
    return render(request, 'paginaweb/nosotros.html')

#paginas de blogs

def blogs(request):
    return render(request, 'blogs/index.html')
    
def crear_blogs(request):
    return render(request, 'blogs/crear.html')    
    
def editar(request):
    return render(request, 'blogs/editar.html')      
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    