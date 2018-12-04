from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

def about_us(request): #About us page
    return render(request,'pages/about_us.html')
