from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('adverts/', include('adverts.urls')),
    path('admin/', admin.site.urls),
    # path('api/', include('adverts.api.urls')),
    path('api/geo/', include('geo.urls'))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
