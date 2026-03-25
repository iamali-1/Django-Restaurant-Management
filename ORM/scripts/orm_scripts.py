from ORM.models import Restaurant, Rating, Sale, Staff
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
from pprint import pprint
from django.db.models import Prefetch


def run():

    restaurant = Restaurant.objects.get(pk = 21)
    print(restaurant.staff_set.all())
