from django import forms
from django.utils.translation import ugettext_lazy
from django.core.exceptions import ValidationError

# from phonenumber_field.formfields import PhoneNumberField


forms.Field.default_error_messages = {
    'required': ugettext_lazy('To pole jest wymagane'),
}


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
        """ Price_to must be greater then Price_from
        """
        price_to = self.cleaned_data.get('price_to')
        if price_to:
            price_form = self.cleaned_data.get('price_from')
            if price_form:
                if int(price_to) <= int(price_form):
                    #  Price range is invalid
                    raise ValidationError("Zakres cenowy jest niepoprawny")
        return price_to


class ReportAdvertForm(forms.Form):
    """
        Form allows visitor to report advert, message is send via email to the site admin
    """
    ESTATE_TYPES = (
        ('Dom', 'Dom'),
        ('Działka', 'Działka'),
        ('Mieszkanie', 'Mieszkanie'),
        ('Inwestycja', 'Inwestycja'),
    )
    ADVERT_TYPES = (
        ('Sprzedaż', 'Sprzedaż'),
        ('Wynajem', 'Wynajem'),
    )
    # Visitor's data
    name = forms.CharField(label='Imię', min_length=2, max_length=20, required=True,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Imię*'}))
    surname = forms.CharField(label='Nazwisko', min_length=2, max_length=20, required=True,
                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nazwisko*'}))
    phone = forms.CharField(label="Telefon", help_text='Bez spacji i/lub znaków specjalnych',
                             required=True, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                          'placeholder': 'Telefon*'}))
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'class': 'form-control',
                                                                            'placeholder': 'E-mail'}))

    # Advert data
    type = forms.ChoiceField(label='Oferta', choices=ADVERT_TYPES, required=True,
                             widget=forms.Select(attrs={'class': 'form-control'}))
    estate = forms.ChoiceField(label='Rodzaj', choices=ESTATE_TYPES, required=True,
                               widget=forms.Select(attrs={'class': 'form-control'}))
    location = forms.CharField(label='Lokalizacja', help_text='Miasto, Dzielnica', required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Lokalizacja*'}))
    size = forms.DecimalField(label='Pow.całkowita[m2]', min_value=0, max_digits=8, decimal_places=1, required=True,
                              widget=forms.NumberInput(attrs={'class': 'form-control',
                                                              'placeholder': 'Pow.całkowita* [m2]:',
                                                              'step': 0.5}))
    price = forms.DecimalField(label='Cena', min_value=0, max_digits=10, decimal_places=2, required=False,
                               widget=forms.NumberInput(attrs={'class': 'form-control',
                                                               'placeholder': 'Cena [zł]:',
                                                               'step': 1.0}))
