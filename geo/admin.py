from django.contrib import admin
from django.contrib.admin.decorators import register

from .models import Location, Address

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


