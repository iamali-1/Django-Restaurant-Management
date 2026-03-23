from django.shortcuts import render
from .forms import RestaurantForm
from .models import Restaurant, Rating, Sale


# Create your views here.
def index(request):
    restaurants = Restaurant.objects.all()
    context = {"restaurants": restaurants}
    return render(request, "index.html", context)
