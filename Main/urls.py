from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

app_name = 'Main'

urlpatterns = [
    path('', index, name='index'),
    path('busket', Busket.as_view(), name='busket'),
    path('watched', watched, name='watched'),
    path('profile', profile, name='profile'),
    path('profile', profile, name='profile'),
    path('billing', billing, name='billing'),
    path('dashboard', dashboard, name='dashboard'),
    path('become_advance_prime_user', become_advance_prime_user, name='become_advance_prime_user'),
    path('become_prime_user', become_prime_user, name='become_prime_user'),
]