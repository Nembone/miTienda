from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cart/', include(('cart.urls', 'cart'), namespace='cart')),
    url(r'^orders/', include(('orders.urls', 'orders'), namespace='orders')),
    url(r'^', include(('shop.urls', 'shop'), namespace='shop')),
    path('', include('pwa.urls')),
    url(r'^webpush/', include('webpush.urls')),   
]



 


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
