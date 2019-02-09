from django.contrib import admin
from django.contrib.admin.decorators import register

from .models import Location, Address, City, Country

@register(Location)
class LocationAdmin(admin.ModelAdmin):
    class Meta:
        model = Location
        exclude = []


@register(Address)
class AddressAdmin(admin.ModelAdmin):
    class Meta:
        model = Address
        exclude = []


@register(City)
class AddressAdmin(admin.ModelAdmin):
    class Meta:
        model = City
        exclude = []


@register(Country)
class AddressAdmin(admin.ModelAdmin):
    class Meta:
        model = Country
        exclude = []


