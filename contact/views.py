from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.
def contact(request):
    return render(request,'contact.html')
