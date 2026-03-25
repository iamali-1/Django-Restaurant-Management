from ORM.models import Restaurant, Rating, Sale, Staff, StaffRestaurant
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
from pprint import pprint
from django.db.models import Prefetch
import random


def run():

    staff, created = Staff.objects.get_or_create(name="John Wick")
    staff.restaurant.set(
        Restaurant.objects.all()[:10],
        through_defaults={"salary": random.randint(20_000, 80_000)},
    )
