from django.shortcuts import render

# Create your views here.
def blog_home(request):
    return render(request,'blog/blog_home.html')

def blog_category(request, category):
    return render(request,'blog/blog_home.html')

def blog_post(request, category, post_id):
    return render(request,'blog/blog_home.html')
