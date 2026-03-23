from ORM.models import Restaurant, Rating, Sale
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
from pprint import pprint


def run():

    restaurants = Restaurant.objects.all()
    pprint(restaurants)
    pprint(connection.queries)
