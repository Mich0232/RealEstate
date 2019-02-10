from django.shortcuts import render
from django.http import JsonResponse

from .models import Advert
from .forms import AdvertForm
from geo.models import QuickFilterLocation, City


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
    locations = QuickFilterLocation.objects.all().order_by('city__name')
    return render(request, template_name='adverts/homepage.html', context={'adverts': adverts,
                                                                           'locations': locations,
                                                                           'current_location': qfl})

def add_advert(request):
    form = AdvertForm()
    return render(request, 'adverts/add_advert.html', {'form': form})


DEFAULT_CITY = 'CRACOW'

def get_pin_locations_ajax(request):
    data = {'success': False}
    if request.is_ajax():
        filter_city = request.GET.get('current_path').strip('/').split('/')[-1].upper()
        filter_location = QuickFilterLocation.objects.filter(code=filter_city)
        qfl = filter_location.first() if filter_location.exists() else QuickFilterLocation.objects.get(code=DEFAULT_CITY)
        adverts = Advert.objects.filter(address__city=qfl.city).select_related('address__cords')
        cords = [advert.address.cords.as_list for advert in adverts]
        data.update({'success': True,
                     'latlng': qfl.latlng,
                     'cords': cords})
    return JsonResponse(data)
