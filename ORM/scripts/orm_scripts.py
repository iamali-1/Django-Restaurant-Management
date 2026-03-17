from ORM.models import Restaurant
from django.utils import timezone


def run():
    restaurant = Restaurant.objects.all()
    print(restaurant)