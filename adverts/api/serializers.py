""" Rest Api serializers classes
"""
from rest_framework import serializers

from ..models import Advert


class AdvertSerializer(serializers.ModelSerializer):
    """ Serialize Advert object"""
    class Meta:
        model = Advert
        fields = ('title', 'type', 'estate', 'size', 'price', 'location')
