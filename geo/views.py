from django.http import JsonResponse
from django.db.models import Q

from .models import Address


def geo_lookup(request):
    data = {'matches': []}
    if request.is_ajax():
        term = request.GET.get('term')
        matches = Address.objects.filter(Q(street__icontains=term) |
                                         Q(city__name__icontains=term)).distinct()
        if matches.exists():
            display_names = []
            cords = []
            for match in matches:
                display_names.append(match.display_address)
                cords.append(match.cords.as_list)
            data.update({'names': display_names,
                         'cords': cords})
    return JsonResponse(data)
