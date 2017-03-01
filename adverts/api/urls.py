""" Rest API urls module"""
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^adverts/$', views.AdvertListView.as_view(), name='list_api_url'),
    url(r'^adverts/(?P<pk>\d+)/$', views.AdvertDetailView.as_view(), name='detail_api_url'),
]
