from django.urls import path
from. views import index,shop,shop_detail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',index,name='index'),
    path('shop',shop,name='shop'),
    path('shop-detail/<int:pk>/',shop_detail, name='shop_detail')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

