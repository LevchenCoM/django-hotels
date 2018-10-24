from django.shortcuts import render
from django.http import HttpResponse
from apartments.models import Apartment, ApartmentImage

# Create your views here.
def home(request):
    apartments = Apartment.objects.filter(is_active = True)
    context = {'apartments':apartments}

    return render(request,'home.html', context)
