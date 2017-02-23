from django import forms
from django.core.exceptions import ValidationError

from .models import Advert


class SearchBox(forms.Form):
    """
        Search form for Advert objects
    """
    ESTATE_TAGS_IDS = (
        (0, 'Dowolne'),
        (1, 'Dom'),
        (2, 'Działka'),
        (3, 'Mieszkanie'),
        (4, 'Inwestycja'),
    )
    ADVERT_TAGS_IDS = (
        (0, 'Dowolne'),
        (5, 'Sprzedaż'),
        (6, 'Wynajem'),
    )
    type = forms.ChoiceField(label="Typ", choices=ADVERT_TAGS_IDS, required=False,
                             widget=forms.Select(attrs={'class': 'form-control'}))
    estate = forms.ChoiceField(label="Nieruchomość", choices=ESTATE_TAGS_IDS, required=False,
                               widget=forms.Select(attrs={'class': 'form-control'}))
    price_from = forms.IntegerField(label="Cena min", min_value=0, required=False,
                                    widget=forms.NumberInput(attrs={'class': 'form-control'}))
    price_to = forms.IntegerField(label="Cena max", min_value=0, required=False,
                                  widget=forms.NumberInput(attrs={'class': 'form-control'}))
    location = forms.CharField(label='Miasto', required=False,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_price_to(self):
        price_to = self.cleaned_data['price_to']
        if price_to:
            if self.cleaned_data['price_from']:
                if int(price_to) <= int(self.cleaned_data['price_from']):
                    raise ValidationError("Zakres cenowy jest niepoprawny")
        return price_to
