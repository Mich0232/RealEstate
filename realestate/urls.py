from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from adverts.views import (
    homepage as homepage_view,
    get_pin_locations_ajax as pin_locations
)

urlpatterns = [
    path('', homepage_view, name='homepage'),
    path('city/<slug:city_code>/', homepage_view, name='homepage_with_code'),
    path('pin_locations/', pin_locations, name='pin_locations'),
    path('admin/', admin.site.urls),
    path('api/', include('adverts.api.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
