from django.urls import path, include
from .views import (
homepage as homepage_view,
get_pin_locations_ajax as pin_locations,
add_advert
)

urlpatterns = [
    path('all/', homepage_view, name='homepage'),
    path('city/<slug:city_code>/', homepage_view, name='homepage_with_code'),
    path('add/', add_advert, name='add_advert'),
    # AJAX
    path('pin_locations/', pin_locations, name='pin_locations'),
]
