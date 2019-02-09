from django.contrib import admin
from django.contrib.admin.decorators import register

from .models import Location, Address, City, Country, QuickFilterLocation

admin.site.register(Location)
admin.site.register(Address)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(QuickFilterLocation)

