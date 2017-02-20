from django.contrib import admin

from .models import Advert, Images


class AdvertImage(admin.TabularInline):
    """
        Advert additional images objects
    """
    model = Images
    extra = 1
    exclude = ['height_field', 'width_field']


class AdvertAdmin(admin.ModelAdmin):
    """
        Advert models admin
    """
    inlines = [AdvertImage, ]
    list_filter = ('type', 'estate')
    search_fields = ('location', )


admin.site.register(Advert, AdvertAdmin)
