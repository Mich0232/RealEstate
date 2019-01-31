import factory
import datetime
import itertools
from random import randrange

import pytz
from django.contrib.auth.models import User
from factory import fuzzy
from django.contrib.auth import get_user_model
from django.utils import timezone
from adverts.models import Advert, AdvertDetail, AdvertStatus


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    username = factory.LazyAttribute(lambda a: '{0}_{1}'.format(a.first_name, a.last_name).lower())
    email = factory.Sequence(lambda n: 'user{0}@example.com'.format(n))
    password = 'secret'

CITIES = [
    'Warszawa',
    'Oslo',
    'Berlin',
    'Madryt',
]

COUNTRIES = [
    'Poland',
    'Germany',
    'Spain',
    'Finland',
]


class AdvertStatusFactory(factory.DjangoModelFactory):
    class Meta:
        model = AdvertStatus

    name = factory.fuzzy.FuzzyText(length=5)
    created = factory.fuzzy.FuzzyDateTime(start_dt=datetime.datetime(2000, 1, 1, tzinfo=pytz.UTC))


_HEATING = [x[0] for x in AdvertDetail.HEATING_TYPES]
_WINDOWS = [x[0] for x in AdvertDetail.WINDOWS]
_FURNITURE = [x[0] for x in AdvertDetail.FURNITURE]
class AdvertDetailFactory(factory.DjangoModelFactory):
    class Meta:
        model = AdvertDetail

    heating = factory.fuzzy.FuzzyChoice(_HEATING)
    windows = factory.fuzzy.FuzzyChoice(_WINDOWS)
    statuses = factory.SubFactory(AdvertStatusFactory)


LOCATIONS = ["{}, {}".format(city, country) for city in CITIES for country in COUNTRIES]
TYPES = [x[0] for x in Advert.ADVERT_TYPES]
ESTATE_TYPES = [x[0] for x in Advert.ESTATE_TYPES]
class AdvertFactory(factory.DjangoModelFactory):
    class Meta:
        model = Advert

    # owner = factory.SubFactory(UserFactory)
    title = factory.Sequence(lambda s: "advert_{}".format(s))
    description = "advert description..."
    location = factory.fuzzy.FuzzyChoice(LOCATIONS)
    type = factory.fuzzy.FuzzyChoice(['sell', 'rent'])
    estate = factory.fuzzy.FuzzyChoice(ESTATE_TYPES)
    price = factory.fuzzy.FuzzyDecimal(1000, 100000)
    size = factory.fuzzy.FuzzyDecimal(10, 250, precision=1)
    plot_size = factory.fuzzy.FuzzyDecimal(100, 2000, precision=1)
    # created = factory.fuzzy.FuzzyDate(datetime.date(year=2000, month=1, day=10))
    # updated = factory.fuzzy.FuzzyDate(datetime.date(year=2000, month=1, day=10))
    # details = factory.RelatedFactory(AdvertDetail)
