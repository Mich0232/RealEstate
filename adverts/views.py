from django.shortcuts import render

from .models import Advert


def homepage(request):
    """
        Homepage view
    """
    return render(request, template_name='adverts/homepage.html')


def adverts_list(request):
    """
        List of all adverts view
    """
    adverts = Advert.objects.all()
    return render(request, template_name='adverts/advert_list.html', context={'adverts': adverts})


def advert_details(request, advert_id):
    """
        Advert details view
    """
    advert = Advert.objects.get(id=advert_id)
    images = advert.images.all()
    return render(request, template_name='adverts/advert_detail.html', context={'advert': advert, 'images': images})
