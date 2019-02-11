from django import forms

from .models import Location, Address

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = (
            'lat',
            'lng'
        )

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = (
            'street',
            'building'
        )
