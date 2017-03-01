""" Advert app urls """
from django.conf.urls import url

from .views import (
    adverts_list,
    advert_details,
    advert_add,
    advert_add_success
)


urlpatterns = [
    url(r'^list/$', adverts_list, name='advert_list_url'),
    url(r'^add/$', advert_add, name='advert_add'),
    url(r'^add/success/$', advert_add_success, name='advert_add_success'),
    url(r'^detail/(?P<advert_id>\d+)/$', advert_details, name='advert_details_url'),
]
