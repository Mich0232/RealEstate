from django.urls import path

from .views import geo_lookup

urlpatterns = [
    path('lookup/', geo_lookup, name='geo_lookup')
]
