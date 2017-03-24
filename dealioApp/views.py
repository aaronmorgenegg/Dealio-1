from django.shortcuts import render
from dealioApp.models import Restaurant
from django.views.generic.edit import CreateView, UpdateView
# Create your views here.


def index(request):
    return render(request, 'dealioApp/home.html') #render looks in templates directory


def restaurants(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'dealioApp/restaurants.html', {'restaurants': restaurants}) #render looks in templates directory #can pass in content into render() such as dictionaries


def promotions(request, restaurant_id):#pass in a restaurant's id into this view to access its promotions via getPromotions
    restaurant = Restaurant.objects.get(id=restaurant_id)
    return render(request, 'dealioApp/promotions.html', {'restaurant': restaurant})

def ownerLogin(request):
    return render(request, 'dealioApp/ownerLogin.html')

class RestaurantCreate(CreateView):
    model = Restaurant
    fields = ['name', 'proms', 'category', 'review_link']

class RestaurantUpdate(UpdateView):
    model = Restaurant
    fields = ['name', 'proms', 'category', 'review_link']

def placefinder(request):
    return render(request, 'dealioApp/placefinder.html')
