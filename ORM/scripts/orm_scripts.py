from ORM.models import Restaurant, Rating, Sale
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
from pprint import pprint


def run():

    user = User.objects.first()
    restaurant = Restaurant.objects.first()

    rating, created = Rating.objects.get_or_create(
        user=user, restaurant=restaurant, rating=4
    )

    pprint(connection.queries)
