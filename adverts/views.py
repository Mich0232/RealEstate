from django.shortcuts import render

from .models import Advert, AdvertDetail
from .forms import SearchBox


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
            tag_id = []
            max_, min_ = 0, 0
            if form.cleaned_data['type'] != '0':
                tag_id.append(form.cleaned_data['type'])
            if form.cleaned_data['estate'] != '0':
                tag_id.append(form.cleaned_data['estate'])
            adverts = Advert.search.tagged_with(tag_id)  # Filter adverts by given tags
            if form.cleaned_data['price_from']:
                min_ = form.cleaned_data['price_from']
            if form.cleaned_data['price_to']:
                max_ = form.cleaned_data['price_to']
            adverts = adverts.price_range(min_, max_)  # Filters prices
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
