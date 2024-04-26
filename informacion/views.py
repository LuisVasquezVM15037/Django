from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request, 'paginaweb/inicio.html')


def nosotros(request):
    return render(request, 'paginaweb/nosotros.html')


def blogs(request):
    return render(request, 'blogs/index.html')
    