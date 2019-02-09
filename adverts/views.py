from django.shortcuts import render
from django.http import JsonResponse

from .models import Advert


def homepage(request):
    """
        Homepage view
    """
    adverts = Advert.objects.all()
    locations = ['Kraków', 'Warszawa', 'Wrocław']
    return render(request, template_name='adverts/homepage.html', context={'adverts': adverts,
                                                                           'locations': locations})

def get_pin_locations_ajax(request):
    data = {'success': False}
    if request.is_ajax():
        adverts = Advert.objects.all().select_related('address__cords')
        cords = [advert.address.cords.as_list for advert in adverts]
        data.update({'success': True,
                     'cords': cords})
    return JsonResponse(data)
