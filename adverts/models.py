from django.db import models
from django.core.urlresolvers import reverse


class Advert(models.Model):
    """
        Advert model
    """
    ESTATE_TYPES = (
        ('house', 'Dom'),
        ('plot', 'Działka'),
        ('flat', 'Mieszkanie'),
        ('investment', 'Inwestycja'),
    )
    ADVERT_TYPES = (
        ('sell', 'Sprzedaż'),
        ('rent', 'Wynajem'),
    )
    title = models.CharField(max_length=250, verbose_name='Tytuł')
    description = models.TextField(max_length=2000, verbose_name='Opis')
    location = models.CharField(max_length=30, verbose_name='Lokacja', blank=True)
    type = models.CharField(max_length=10, choices=ADVERT_TYPES, verbose_name='Typ ogłoszenia')
    estate = models.CharField(max_length=12, choices=ESTATE_TYPES, verbose_name='Typ nieruchomości')
    size = models.DecimalField(max_digits=8, decimal_places=1, verbose_name='Rozmiar')
    plot_size = models.DecimalField(max_digits=8, decimal_places=1, verbose_name='Rozmiar działki', default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Cena')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('type', )
        verbose_name = 'Oferta'
        verbose_name_plural = 'Oferty'

    def __str__(self):
        return "({}) - {} | {}m2 | {}zł".format(dict(self.ESTATE_TYPES)[self.estate],
                                                self.location, self.size, self.price)

    def get_absolute_url(self):
        return reverse(viewname='advert_details_url', args=[self.id])


def upload_directory(instance, filename):
    return "%s/%s" % (instance.pk, filename)


class Images(models.Model):
    """
        Image model for Advert photo gallery. (thumbnail can only be one per Advert)
    """
    advert = models.ForeignKey(Advert, related_name='images', default=None)
    image = models.ImageField(upload_to=upload_directory, height_field='height_field',
                              width_field='width_field', verbose_name="Zdjęcie")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    thumbnail = models.BooleanField(default=False, verbose_name="Miniaturka")

    class Meta:
        verbose_name = "Zdjęcie"
        verbose_name_plural = "Zdjęcia"
