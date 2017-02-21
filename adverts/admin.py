from django.contrib import admin

from .models import Images, AdvertDetail


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
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'location', 'type', 'estate', 'size', 'plot_size', 'price', 'tags')
        }),
        ('Więcej', {
            'classes': ('collapse',),
            'fields': ('heating', 'windows', 'furniture', 'balcony')
        })
    )
    prepopulated_fields = {'tags': ('type', 'estate',)}
    ordering = ['-updated']
    list_filter = ('type', 'estate', 'heating', 'furniture')
    search_fields = ('location', )

    def save_model(self, request, obj, form, change):
        """ Custom save due to assigning correct tags """
        form.cleaned_data['tags'] = form.cleaned_data['tags'][0].split('-')
        print(form.cleaned_data['tags'])
        obj.save()


admin.site.register(AdvertDetail, AdvertAdmin)
