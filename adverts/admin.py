from django.contrib import admin
from django.contrib.admin.decorators import register

from .models import Advert

@register(Advert)
class Advert(admin.ModelAdmin):
    """
        Advert additional images objects
    """
    class Meta:
        model = Advert
        exclude = []
