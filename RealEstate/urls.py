"""RealEstate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from adverts import views as adverts_views

urlpatterns = [
    url(r'^$', adverts_views.homepage, name='homepage_url'),
    url(r'^admin/', admin.site.urls),
    url(r'^contact/$', adverts_views.contact, name='contact_url'),
    url(r'^adverts/$', adverts_views.adverts_list, name='advert_list_url'),
    url(r'^add-advert/$', adverts_views.advert_add, name='advert_add'),
    url(r'^add-advert/success/$', adverts_views.advert_add_success, name='advert_add_success'),
    url(r'^adverts/(?P<advert_id>\d+)/$', adverts_views.advert_details, name='advert_details_url'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
