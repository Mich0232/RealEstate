from django.db import models


class Location(models.Model):
    lat = models.CharField(max_length=16)
    lng = models.CharField(max_length=16)

    @property
    def as_list(self):
        return [self.lat, self.lng]


class Address(models.Model):
    street = models.CharField(max_length=100)
    building = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    cords = models.ForeignKey('geo.Location',
                              on_delete=models.SET_NULL,
                              null=True,
                              related_name='addresses')

