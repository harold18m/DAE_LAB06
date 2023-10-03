from django.shortcuts import render

# Create your views here.
from .models import Producto,Categoria
def index(request):
    product_list = Producto.objects.order_by('nombre')
    categorias = Categoria.objects.order_by('nombre')
    context = {
        'product_list' : product_list,
        'categorias' : categorias,
    }
    return render(request,'index.html',context)

def producto(request):
    return render(request,'producto.html')