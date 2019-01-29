from random import randrange
from django.contrib.auth.models import User
from factories.account_factories import AdvertFactory


def run(amount):
    for x in range(int(amount)):
        user_id = randrange(1, User.objects.count())
        user = User.objects.get(pk=user_id)
        AdvertFactory.create(owner=user)
