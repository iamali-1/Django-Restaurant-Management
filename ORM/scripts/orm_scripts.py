from ORM.models import Restaurant, Rating, Sale
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
from pprint import pprint


def run():

    restaurants = Rating.objects.filter(restaurant__name__startswith = 'c')
    pprint(restaurants)
    pprint(connection.queries)
