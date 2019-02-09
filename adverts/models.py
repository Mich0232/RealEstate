from django.db import models

HOUSE = 'house'
FLAT = 'flat'
INVESTMENT = 'investment'
PLOT = 'plot'


ESTATE_TYPES = (
    (HOUSE, 'House'),
    (FLAT, 'Flat'),
    (INVESTMENT, 'Investment'),
    (PLOT, 'Plot'),
)


class Advert(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    estate_type = models.CharField(max_length=10, choices=ESTATE_TYPES)
    address = models.ForeignKey('geo.Address', on_delete=models.SET_NULL, null=True, related_name='adverts')

