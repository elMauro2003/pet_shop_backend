from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('apps.accounts.api.routers.routes')),
    # path('api/pets/', include('pets.urls')),
    # path('api/blog/', include('blog.urls')),
    # path('api/shop/', include('shop.urls')),
    # path('api/events/', include('events.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)