from django.shortcuts import render
from .models import *

def index (request):
    products = Products.objects.all()
    return render(request, 'index.html', {'products': products})

def shop (request):
    return render(request, 'shop.html')



def shop_detail (request,pk):
    shop_detail= Products.objects.get(pk=pk)
    return render(request, 'shop-detail.html', {'shop_detail': shop_detail})

# Create your views here.
