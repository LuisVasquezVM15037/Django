from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect


# Create your views here.

def inicio(request):
    return render(request, 'paginaweb/inicio.html')
@login_required
def inicio2(request):
    return render(request, 'paginaweb/inicio2.html')

#  #aqui van las demas 2023,2022,2021,2020
def tra2023(request):
    return render(request, 'paginaweb/tra2023.html')

def tra2022(request):
    return render(request, 'paginaweb/tra2022.html')

def tra2021(request):
    return render(request, 'paginaweb/tra2021.html')

def tra2020(request):
    return render(request, 'paginaweb/tra2020.html')















def nosotros(request):
    return render(request, 'paginaweb/nosotros.html')

#paginas de blogs

def blogs(request):
    return render(request, 'blogs/index.html')
    
def crear_blogs(request):
    return render(request, 'blogs/crear.html')    
    
def editar(request):
    return render(request, 'blogs/editar.html')    

def exit(request):
    logout(request)
    return redirect('inicio')  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    