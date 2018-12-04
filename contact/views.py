from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from .forms import ContactForm
# Create your views here.
def contact(request):
    
    if request.method == 'POST':
        if request.user.is_authenticated:
            post_data = {'name':request.user.get_username(), 'email': request.user.get_username(), \
                         'subject': request.POST['subject'], 'message': request.POST['message']}
            contact_form = ContactForm(post_data)
        else:
            contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return redirect('/contact/')
    else:
        contact_form = ContactForm()

    return render(request,'pages/contact.html', {'form':contact_form})
