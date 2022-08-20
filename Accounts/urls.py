from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
app_name = 'Accounts'

urlpatterns = [
	path('login', signin, name='signin'),
    path('register', signup, name='signup'),
    path('logout', Logout, name='logout'),
]