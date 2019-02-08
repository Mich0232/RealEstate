from django.shortcuts import render

from .models import Advert


def homepage(request):
    """
        Homepage view
    """
    adverts = Advert.objects.all()
    locations = ['Kraków', 'Warszawa', 'Wrocław']
    return render(request, template_name='adverts/homepage.html', context={'adverts': adverts,
                                                                           'locations': locations})
