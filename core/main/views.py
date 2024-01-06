from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def services(request):
    return render(request, 'services.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def blog_details(request):
    return render(request, 'blog_details.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')