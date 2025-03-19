from django.shortcuts import render
from .models import Product

# Create your views here.
def home(request):
    return render (request,'electronics/home.html')

def product_detail(request):
    prod =  Product.objects.all()
    return render (request, 'electronics/product_detail.html', {"prod":prod})

