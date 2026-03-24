from ORM.models import Restaurant, Rating, Sale
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
from pprint import pprint
from django.db.models import Prefetch


def run():
    # Get all 5 star ratings and fetch all sales for restaurants with 5 star ratings
    month_ago = timezone.now() - timezone.timedelta(days=30)
    monthly_sales = Prefetch(
        "sales", queryset=Sale.objects.filter(datetime__gte=month_ago)
    )
    restaurants = Restaurant.objects.prefetch_related("ratings", monthly_sales)
    pprint(restaurants)
    pprint(connection.queries)
