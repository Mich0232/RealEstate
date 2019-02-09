from django.shortcuts import render
from django.http import JsonResponse

from .models import Advert
from geo.models import QuickFilterLocation


def homepage(request, city_code=None):
    """
        Homepage view
    """
    if city_code:
        qfl = QuickFilterLocation.objects.get(code__iexact=city_code)
        adverts = Advert.objects.filter(address__city=qfl.city)
    else:
        qfl = None
        adverts = Advert.objects.all()
    locations = QuickFilterLocation.objects.all()
    return render(request, template_name='adverts/homepage.html', context={'adverts': adverts,
                                                                           'locations': locations,
                                                                           'current_location': qfl})

def get_pin_locations_ajax(request):
    data = {'success': False}
    if request.is_ajax():

        path = request.GET.get('current_path').strip('/')
        city = path.split('/')[1] if path else None
        qfl = QuickFilterLocation.objects.get(code__iexact=city) if city else QuickFilterLocation.objects.first()
        adverts = Advert.objects.filter(address__city=qfl.city).select_related('address__cords')
        cords = [advert.address.cords.as_list for advert in adverts]
        data.update({'success': True,
                     'latlng': qfl.latlng,
                     'cords': cords})
    return JsonResponse(data)
