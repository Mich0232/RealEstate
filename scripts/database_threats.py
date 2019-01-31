from copy import copy
import pytz

from datetime import timedelta, datetime
from random import randrange

import gevent
from django.contrib.auth.models import User
from django.db import transaction
from psycogreen import gevent as psy_gevent
psy_gevent.patch_psycopg()

import os

from adverts.models import Advert

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "RealEstate.settings")

import django
django.setup()

from django import db
from django.db.models import Q
from django.utils import timezone

class NonExistingModel(Exception):
    def __init__(self, message):
        super(NonExistingModel, self).__init__(message)


def random_date(start, end):
    delta = end - start

    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_seconds = randrange(int_delta)
    return (start + timedelta(seconds=random_seconds)).replace(tzinfo=pytz.UTC)


def get_connection_from_pool(no):
    conn_alias = 'xd_{}'.format(no)
    db.connections.databases[conn_alias] = copy(db.connections.databases['default'])
    return conn_alias

sql = 'Select owner.username, advert.estate, count(advert.estate) as am from adverts_advert advert JOIN auth_user owner on advert.owner_id=owner.id group by owner.username, advert.estate order  by am desc;'

def foo(arg, limit):
    print('Running thread no {}'.format(arg))
    conn_alias = get_connection_from_pool(arg)
    # with db.connections[conn_alias].cursor() as cursor:
    #     cursor.execute(sql)
    Advert.objects.using(conn_alias).all()


def count(arg, model):
    if not model:
        return 0

    print('Running count no.{}'.format(arg))
    conn_alias = get_connection_from_pool(arg)
    return model.objects.using(conn_alias).count()


def select(arg, model, offset=None, limit=None):
    if not model:
        raise NonExistingModel
    print('Running count no.{}'.format(arg))
    conn_alias = get_connection_from_pool(arg)

    # qs = model.objects.none()

    if not offset and not limit:
        qs = model.objects.using(conn_alias).all()
    if offset:
        qs = model.objects.using(conn_alias).filter(pk__gte=offset)
    if limit:
        qs = model.objects.using(conn_alias).filter(pk__lte=limit)
    global_list.extend(list(qs))

global_list = []
global_list_one = []

start_time = datetime(2004, 1, 1, tzinfo=pytz.UTC)
end_time = datetime(2006, 12, 31, tzinfo=pytz.UTC)

def select_p1(arg, model):
    conn_alias = get_connection_from_pool(arg)
    global_list.extend(list(model.objects.using(conn_alias).filter(created__range=(start_time, end_time),
                                                                   owner__first_name__istartswith='a')))

def select_p2(arg, model):
    conn_alias = get_connection_from_pool(arg)
    global_list.extend(list(model.objects.using(conn_alias).filter(location__icontains='Poland')))


def run():
    # start_date = datetime(year=2000, month=1, day=1)
    # end_date = datetime.now()
    # print(start_date, end_date)
    # with transaction.atomic():
    #     for advert in Advert.objects.all().iterator():
    #         advert.created = random_date(start_date, end_date)
    #         advert.save()
    # return

    a = timezone.now()
    middle = 1112
    gevent.joinall([
        gevent.spawn(select_p1, 1, Advert),
        gevent.spawn(select_p2, 2, Advert),
    ])
    b = timezone.now()
    print('execution time: {}s'.format((b - a).total_seconds()))
    c = timezone.now()
    # global_list_one.extend(list(Advert.objects.filter(owner__first_name__in=['Phillip', 'Austin'])))
    Advert.objects.filter(Q(created__range=(start_time, end_time),
                            owner__first_name__istartswith='a') |
                          Q(location__icontains='Poland'))
    global_list_one.extend(list())
    d = timezone.now()
    print('execution time: {}s'.format((d - c).total_seconds()))
    print(len(global_list))
    print(len(global_list_one))