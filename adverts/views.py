import difflib
import operator

from functools import reduce

from django.db.models import Q
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings

from .models import Advert, AdvertDetail
from .forms import SearchBox, ReportAdvertForm


def homepage(request):
    """
        Homepage view
    """
    return render(request, template_name='adverts/homepage.html')


def adverts_list(request):
    """
        List of all adverts, with filtering form.
        User can filter by: type of advert, type of estate, price range, and location (city).
        If location is given - it search for best match in locations of all adverts.
    """
    # TODO: Scaling for mobile
    form = SearchBox()
    if request.method == 'POST':
        form = SearchBox(request.POST)
        if form.is_valid():
            # Search engine
            # Filter adverts by given tags
            selected_tags = [form.cleaned_data['type'], form.cleaned_data['estate']]
            adverts = Advert.search.tagged_with(selected_tags)
            # Filters prices
            adverts = adverts.price_range(form.cleaned_data['price_from'], form.cleaned_data['price_to'])
            # Location filter
            if form.cleaned_data['location']:
                # All locations (cities) form adverts
                locations = set([location.split(',')[0] for location in list(adverts.values_list('location',
                                                                                                 flat=True))])
                best_locations = difflib.get_close_matches(form.cleaned_data['location'], locations)
                if best_locations:
                    # If possible match was found
                    query = reduce(operator.or_, [Q(location__contains=loc) for loc in best_locations])
                    adverts = adverts.filter(query)
                else:
                    # Location not found message
                    error = form.cleaned_data['location']
                    return render(request, template_name='adverts/advert_list.html',
                                  context={'form': form, 'adverts': adverts, 'error': error})
        else:
            adverts = Advert.objects.all()
    else:
        adverts = Advert.objects.all()
    return render(request, template_name='adverts/advert_list.html', context={'form': form,
                                                                              'adverts': adverts})


def advert_details(request, advert_id):
    """
        Renders view with Advert info, images carousel and details table.
        Takes Advert object ID.
    """
    advert = Advert.objects.get(id=advert_id)
    images = advert.images.all()
    details = AdvertDetail.objects.get(advert_ptr_id=advert.id)
    return render(request, template_name='adverts/advert_detail.html', context={'advert': advert,
                                                                                'images': images,
                                                                                'details': details})


def advert_add(request):
    """
        Renders a form, with which visitor can report their adverts.
        Form data is send by email to the Admin, for further verification.
    """
    form = ReportAdvertForm()
    if request.method == 'POST':
        form = ReportAdvertForm(request.POST)
        if form.is_valid():
            # Sending email with advert data
            test_receiver = None
            msg_html = render_to_string('adverts/mail/advert_report_message.html', form.cleaned_data)
            msg_text = render_to_string('adverts/mail/advert_report_message.txt', form.cleaned_data)
            send_mail('Zgłoszono nową ofertę', msg_text, settings.EMAIL_HOST_USER, [test_receiver],
                      html_message=msg_html, fail_silently=False)
            # TODO: send mail
            return redirect(to=advert_add_success)
    fields = list(form)
    personal_form, estate_form = fields[:4], fields[4:]
    return render(request, template_name='adverts/report_advert.html', context={'personal_form': personal_form,
                                                                                'estate_form': estate_form})


def contact(request):
    """
        Brand contact page
    """
    return render(request, template_name='adverts/contact.html')


def advert_add_success(request):
    """
        Renders after 'advert_add' form is successfully submitted.
    """
    return render(request, template_name='adverts/report_advert_success.html')
