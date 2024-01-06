from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('blog_details/', views.blog_details, name='blog_details'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    # path('profile/', views.profile, name='profile'),
    # path('calculator/', views.calculator, name='calculator'),
    # Add other paths for your app views
]