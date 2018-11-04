from django.shortcuts import render, redirect
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.http import HttpResponse

def sign_up(request):
    user_creation_form = UserCreationForm()
    if request.method=='POST':
        user_creation_form = UserCreationForm(request.POST)
        # user_form = UserSignUpForm(request.POST)
        if user_creation_form.is_valid():
            username=user_creation_form.cleaned_data['username']
            password=user_creation_form.cleaned_data['password1']
            new_user=User.objects.create_user(username=username,password=password)
            login(request, authenticate(username=username,password=password))
            return redirect('/home')
    return render(request, "user_auth/sign-up.html", {'user_form':user_creation_form})

# def sign_in(request):
#     # user_form=UserSignUpForm()
#     # # user_form = UserCreationForm()
#     # dir(user_form)
#     # if request.method=='POST':
#     #     user_form = UserSignUpForm(request.POST)
#     #     # user_form = UserCreationForm(request.POST)
#     #     if user_form.is_valid():
#     #         username=user_form.cleaned_data['username']
#     #         password=user_form.cleaned_data['password1']
#     #         new_user=User.objects.create_user(username=username,password=password)
#     #         login(request, authenticate(username=username,password=password))
#     #         return redirect('/home')
#     return render(request, "user_auth/sign-up.html", {'user_form':user_form})
