from django import template
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.templatetags.staticfiles import static

register = template.Library()


@register.inclusion_tag('adverts/tags/navbar.html')
def nav_bar():
    """ Renders navigation bar """
    pass


@register.inclusion_tag('adverts/tags/search_box.html')
def search_box():
    """ Renders search box on navigation bar """
    pass


@register.simple_tag()
def get_advert_list_url():
    """
        Returns url for adverts list
    """
    return reverse('advert_list_url')


@register.assignment_tag()
def get_advert_thumbnail(advert):
    """
        Takes Advert object and returns thumbnail image, if no thumbnail - returns first image
        if no image at all returns 'no-photo.jpg'
    """
    photos = advert.images.all()
    if photos:
        for photo in photos:
            if photo.thumbnail:
                return photo.image.url
        return photos[0].image.url
    return static('img/no-photo.jpg')


@register.assignment_tag()
def new_line_advert(loop, per_row=3):
    """
        Return True if current Advert needs to be in new row (3 Adverts per row)
    """
    return True if loop % per_row == 0 else False
