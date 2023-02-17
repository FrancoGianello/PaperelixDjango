from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import Producto, Categoria
# Create your views here.


def index(request):
    return render(
        request, 'paperelix/index.html',
        {
            "categorias": Categoria.getAll(),
            "productos":Producto.objects.order_by('-nombre')[:3]
        }
    )

def producto (request, pk):
    producto =  Producto.objects.get(id=pk)
    relacionados = Producto.relacionados(producto.categoria)
    return render(
        request, 'paperelix/producto.html',
        {
            "producto": producto,
            "relacionados" : relacionados
        }
    )

def categoria (request, nombre):
    categoria = Categoria.objects.get(nombre=nombre)
    return render(
        request, 'paperelix/categoria.html',
        {
            "categoria": categoria,
            "productos" : Producto.objects.filter(categoria=categoria)
        }
    )