from django.shortcuts import render,redirect
from .forms import *
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from store.models import Products
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

@login_required(login_url='/login')
def index (request):
    products = Products.objects.all()
    return render(request, 'index.html', {'products': products})

def shop (request):
    return render(request, 'shop.html')



def shop_detail (request,pk):
    shop_detail= Products.objects.get(pk=pk)
    return render(request, 'shop-detail.html', {'shop_detail': shop_detail})

def cart (request):
    return render(request, 'cart.html')


# def chackout (request):
   
#     return render(request, 'chackout.html',{'chackout':chackout})


def testimonial (request):
    return render(request, 'testimonial.html')

def error (request):
    return render(request, 'error.html')


# def contact(request):
#     return render(request, 'contact.html',{'contact':contact})



def contact(request):
    form = ContactForm (request.POST)
    if request.method =='POST':
        form = ContactForm (request.POST)
        if form.is_valid():
           form.save()
           return redirect('index')
           
    

    return render(request,'contact.html',{'form':form})

def chackout(request):
    form = BillingForm(request.POST)
    if request.method =='POST':
        form = BillingForm (request.POST)
        if form.is_value.pk():
           form.save()
           return redirect('index')
           
    

    return render(request,'chackout.html',{'form':form})


# Create your views here.



def cart_add(request, pk):
    cart = Cart(request)
    product = Products.objects.get(pk=pk)
    cart.add(product=product)
    return redirect("shop_detail",pk=pk)


def item_clear(request, pk):
    cart = Cart(request)
    product = Products.objects.get(pk=pk)
    cart.remove(product)
    return redirect("cart")



def item_increment(request, pk):
    cart = Cart(request)
    product = Products.objects.get(pk=pk)
    cart.add(product=product)
    return redirect("cart")



def item_decrement(request, pk):
    cart = Cart(request)
    product = Products.objects.get(pk=pk)
    cart.decrement(product=product)
    return redirect("cart")



def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")



def cart_detail(request):
    return render(request, 'cart/cart_detail.html')