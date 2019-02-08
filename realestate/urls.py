from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from adverts.views import (
    homepage as homepage_view
)

urlpatterns = [
    url(r'^$', homepage_view, name='homepage_url'),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('adverts.api.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
