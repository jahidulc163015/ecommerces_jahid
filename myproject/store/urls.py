from django.urls import path
from .views import  *
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib import admin  # Django admin module
      
from authentication.views import *  # Import views from the authentication app
from django.conf import settings   # Application settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns  # Static files serving
from django.conf.urls.static import static
from django.conf import settings





urlpatterns = [   
    path('',index,name='index'),
    path('shop',shop,name='shop'),
    path('shop-detail/<int:pk>/',shop_detail,name='shop_detail'),
    path('cart',cart,name='cart'),
    path('chackout',chackout,name='chackout'),
    path('testimonial',testimonial,name='testimonial'),
    path('error',error,name='error'),
    path('contact',contact,name='contact'),
    
    path('cart/add/<int:pk>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:pk>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:pk>/', views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:pk>/',views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)