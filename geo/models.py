from django.db import models


class Location(models.Model):
    lat = models.CharField(max_length=16)
    lng = models.CharField(max_length=16)

    @property
    def as_list(self):
        return [self.lat, self.lng]

    def __str__(self):
        return f"lat:{self.lat}, lng:{self.lng}"


class Address(models.Model):
    street = models.CharField(max_length=100)
    building = models.CharField(max_length=100)
    city = models.ForeignKey('geo.City', on_delete=models.CASCADE, null=True)
    cords = models.ForeignKey('geo.Location',
                              on_delete=models.SET_NULL,
                              null=True,
                              related_name='addresses')

    class Meta:
        verbose_name_plural = 'Addresses'

    @property
    def display_address(self):
        return f"{self.street} {self.building}, {self.city.name}"

    def __str__(self):
        return f"{self.street} {self.building}, {self.city.name}"


class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.ForeignKey('geo.Country', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Cities'

    def __str__(self):
        return f"{self.name}, {self.state}, {self.country.name}"


class Country(models.Model):
    name = models.CharField(max_length=100)
    iso_2_code = models.CharField(max_length=2)

    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name


class QuickFilterLocation(models.Model):
    city = models.ForeignKey('geo.City', on_delete=models.CASCADE)
    code = models.CharField(max_length=20)
    lat = models.CharField(max_length=16)
    lng = models.CharField(max_length=16)

    @property
    def latlng(self):
        return [self.lat, self.lng]

    def __str__(self):
        return f"QFL: {self.city.name}"
