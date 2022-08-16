from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'Paystack'

urlpatterns = [
    path('', initiate_payment, name='initiate_payment'),
]