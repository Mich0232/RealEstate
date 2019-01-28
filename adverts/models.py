from django.db import models
from django.shortcuts import reverse

# from taggit.managers import TaggableManager


class SearchQueryset(models.QuerySet):
    """
        Custom queryset for Advert searching
    """
    def price_range(self, min_, max_):
        query = self
        if min_:
            query = query.filter(price__gte=min_)
        if max_:
            query = query.filter(price__lte=max_)
        return query

    def tagged_with(self, tag_id):
        query = self
        tags = [x for x in tag_id if int(x)]
        if tags:
            for id_ in tags:
                query = query.filter(tags__exact=id_)
        return query


class SearchManager(models.Manager):
    """ Search box Advert manager"""
    def get_queryset(self):
        return SearchQueryset(self.model, using=self._db)

    def price_range(self, min_, max_):
        return self.get_queryset().price_range(min_, max_)

    def tagged_with(self, tag_id):
        return self.get_queryset().tagged_with(tag_id)


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
    size = models.DecimalField(max_digits=8, decimal_places=1, verbose_name='Rozmiar (m2)')
    plot_size = models.DecimalField(max_digits=8, decimal_places=1, verbose_name='Rozmiar działki (m2)', default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Cena (zł)')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Managers
    objects = models.Manager()
    # tags = TaggableManager()
    search = SearchManager()

    def __str__(self):
        return "({}) - {} | {}m2 | {}zł".format(dict(self.ESTATE_TYPES)[self.estate],
                                                self.location, self.size, self.price)

    def get_absolute_url(self):
        return reverse(viewname='advert_details_url', args=[self.id])


def upload_directory(instance, filename):
    """ Return upload directory for images """
    return "%s/%s" % (instance.pk, filename)


class Images(models.Model):
    """
        Image model for Advert photo gallery. (There can only be one thumbnail per Advert)
    """
    advert = models.ForeignKey(Advert, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_directory, height_field='height_field',
                              width_field='width_field', verbose_name="Zdjęcie")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    thumbnail = models.BooleanField(default=False, verbose_name="Miniaturka")

    class Meta:
        verbose_name = "Zdjęcie"
        verbose_name_plural = "Zdjęcia"


class AdvertDetail(Advert):
    """
        Detailed info about Advert
    """
    HEATING_TYPES = (
        ('gas', "Gazowe"),
        ('coal', "Węglowe"),
        ('electric', "Elektryczne"),
        ('city', "Miejskie"),
        ('furnace', "Kominkowe"),
        ('diff', "inne"),
    )
    WINDOWS = (
        ('wooden', 'Drewniane'),
        ('plastic', 'Plastikowe')
    )
    FURNITURE = (
        ('none', "Brak"),
        ('half', "Kuchnia i łazienka"),
        ('full', "Pełne"),
    )
    heating = models.CharField(max_length=10, choices=HEATING_TYPES, blank=True, null=True, verbose_name='Ogrzewanie')
    windows = models.CharField(max_length=8, choices=WINDOWS, blank=True, null=True, verbose_name='Okna')
    furniture = models.CharField(max_length=4, choices=FURNITURE, blank=True, null=True, verbose_name='Umeblowanie')
    balcony = models.BooleanField(blank=True, verbose_name="Balkon")

    class Meta:
        ordering = ('type', )
        verbose_name = 'Oferta'
        verbose_name_plural = 'Oferty'
