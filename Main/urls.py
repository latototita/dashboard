from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

app_name = 'Main'

urlpatterns = [
    path('', index, name='index'),
    path('tables', tables, name='tables'),
    path('profile', profile, name='profile'),
    path('profile', profile, name='profile'),
    path('billing', billing, name='billing'),
    path('dashboard', dashboard, name='dashboard'),
]