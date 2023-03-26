
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    #admin app
    path('admin/', admin.site.urls),

    #home_page app
    path('',include('store.urls')),

    #cart app

    path('cart/', include('cart.urls')),
]

urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)