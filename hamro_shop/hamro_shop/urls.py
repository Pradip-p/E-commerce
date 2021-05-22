
from django.contrib import admin
from django.urls import path, include
# from shop.views import index
from cart.views import card_display
 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include('shop.urls')),
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls')),
    path('user/', include('user.urls')),

] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
