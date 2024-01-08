from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import subprocess

@csrf_exempt
def pushupdate(request):
    if request.method == 'POST':
        # Change to your project directory
        project_directory = '/home/mrsingh29/InProject/core'
        subprocess.run(['git', '-C', project_directory, 'pull'])
        return JsonResponse({'message': 'Webhook received and project updated successfully'})
    else:
        return JsonResponse({'message': 'Pulled'}, status=400)
    

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