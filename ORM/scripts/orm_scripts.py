from ORM.models import Restaurant, Rating, Sale
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
from pprint import pprint


def run():

    restuarant = Restaurant.objects.filter(name__startswith="P")

    restuarant.update(date_opened=timezone.now() - timezone.timedelta(days=365))
    pprint(restuarant)
    pprint(connection.queries)
