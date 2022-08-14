from django.db import models

# Create your models here.
from django.utils import timezone
from django.conf import settings
import datetime
from .product import Product
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from datetime import date


class User(AbstractUser):
	username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
	email = models.EmailField(_('email address'), unique = True)
	first_name = models.CharField(max_length = 15)
	last_name = models.CharField(max_length = 15)
	phone_no = models.CharField(max_length = 10)
	image=models.ImageField(upload_to='media/profile', default='')
    Country=models.CharField(default='',blank=True, max_length=100)
    district=models.CharField(default='1',blank=True,max_length=13)
    Bank=models.CharField(default='',blank=True, max_length=100,unique=True)
    Account_number=models.CharField(max_length=100,default='None',blank=True)
    date_joined= models.DateTimeField(default=timezone.now)
    advertiser=models.BooleanField(default=False)
    prime_user=models.BooleanField(default=False)
    advance_prime_user=models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    def __str__(self):
    	return "{}".format(self.email)

class Watched(models.Model):
	person = models.ForeignKey(
        User, on_delete=models.CASCADE)
	total_ads_watched = models.CharField(max_length = 30)
	date_watched =models.DateTimeField(default=timezone.now)

	class Meta:
        ordering = ('-date_watched', )

class Ads(models.Model):
	file = models.FileField(blank=True, blank=True, null=True)
	description_of_ad= models.TextField()
	button_link= models.CharField(max_length=1000)
	videolink = models.CharField(max_length=1000,blank=True,null=True)
	location = models.ForeignKey(
        Location, on_delete=models.CASCADE)
	prime_price_per_click =  models.IntegerField(default=0.26)
	advance_prime_price_per_click =  models.IntegerField(default=0.45)

