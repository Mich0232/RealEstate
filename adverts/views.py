import difflib
import operator

from functools import reduce

from django.db.models import Q
from django.shortcuts import render

from .models import Advert, AdvertDetail
from .forms import SearchBox

from fuzzywuzzy import process as fuzzy_process


def homepage(request):
    """
        Homepage view
    """
    return render(request, template_name='adverts/homepage.html')


def adverts_list(request):
    """
        List of all adverts view
    """
    form = SearchBox()
    if request.method == 'POST':
        form = SearchBox(request.POST)
        if form.is_valid():
            # Search engine
            # Filter adverts by given tags
            tag_id = [form.cleaned_data['type'], form.cleaned_data['estate']]
            adverts = Advert.search.tagged_with(tag_id)
            # Filters prices
            adverts = adverts.price_range(form.cleaned_data['price_from'], form.cleaned_data['price_to'])
            # Location filter
            if form.cleaned_data['location']:
                # All locations form adverts
                locations = set([location.split(',')[0] for location in list(adverts.values_list('location',
                                                                                                 flat=True))])
                best_locations = difflib.get_close_matches(form.cleaned_data['location'], locations)
                if best_locations:
                    # If possible match was found
                    query = reduce(operator.or_, [Q(location__contains=loc) for loc in best_locations])
                    adverts = adverts.filter(query)
        else:
            adverts = Advert.objects.all()
    else:
        adverts = Advert.objects.all()
    return render(request, template_name='adverts/advert_list.html', context={'form': form,
                                                                              'adverts': adverts})


def advert_details(request, advert_id):
    """
        Advert details view
    """
    advert = Advert.objects.get(id=advert_id)
    images = advert.images.all()
    details = AdvertDetail.objects.get(advert_ptr_id=advert.id)
    return render(request, template_name='adverts/advert_detail.html', context={'advert': advert,
                                                                                'images': images,
                                                                                'details': details})
