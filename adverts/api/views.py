""" Rest API views to receive data
"""
from rest_framework import generics

from ..models import Advert
from .serializers import AdvertSerializer


class AdvertListView(generics.ListAPIView):
    """ Return list of all Adverts """
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer


class AdvertDetailView(generics.RetrieveAPIView):
    """ Return advert details"""
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer
