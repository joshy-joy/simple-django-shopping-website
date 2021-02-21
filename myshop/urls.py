from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^coupons/', include('coupons.urls', namespace='coupons')),
    url(r'^orders/', include('orders.urls', namespace='orders')),
    url(r'^auth/', include('login.urls', namespace="auth")),
    url(r'^', include('shop.urls', namespace='shop')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
