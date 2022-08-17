from django.db import models

# Create your models here.
from django.utils import timezone
from django.conf import settings
import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import date


class User(AbstractUser):
	username = models.CharField(max_length=50,blank=True,null=True,unique=True)
	email = models.EmailField(unique=True)
	first_name = models.CharField(max_length=15)
	last_name = models.CharField(max_length=15)
	phone_no = models.CharField(max_length=10)
	image=models.ImageField(upload_to='media/profile',default='')
	country=models.CharField(blank=True,max_length=100)
	district=models.CharField(max_length=13)
	bank=models.CharField(max_length=100,unique=True)
	prime=models.BooleanField(default=False)
	advance_prime=models.BooleanField(default=False)
	def __str__(self):
		return self.username
        
class Watched(models.Model):
	person = models.ForeignKey(
        User, on_delete=models.CASCADE)
	total_ads_watched = models.CharField(max_length = 30)
	date_watched =models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.person
	class Meta:
		ordering = ('-date_watched', )

class Location(models.Model):
	name= models.CharField(max_length=1000)
	def __str__(self):
		return self.name

class Ads(models.Model):
	file = models.FileField(blank=True,null=True)
	description_of_ad= models.TextField()
	button_link= models.CharField(max_length=1000)
	videolink = models.CharField(max_length=1000,blank=True,null=True)
	location = models.ForeignKey(
        Location, on_delete=models.CASCADE)
	prime_price_per_click =  models.IntegerField(default=0.26)
	advance_prime_price_per_click =  models.IntegerField(default=0.45)
	def __str__(self):
		return self.location