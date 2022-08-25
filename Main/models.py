from django.db import models
# Create your models here.
from django.utils import timezone
from django.conf import settings
import datetime
from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import date
from django.db import models
from django.contrib.auth.models import AbstractUser


class Country(models.Model):
	name= models.CharField(max_length=1000)
	def __str__(self):
		return self.name

class User(AbstractUser):
	username = models.CharField(max_length=50,blank=True,null=True,unique=True)
	email = models.EmailField(unique=True)
	first_name = models.CharField(max_length=15)
	last_name = models.CharField(max_length=15)
	phone_no = models.CharField(max_length=10)
	image=models.ImageField(upload_to='media/profile',default='')
	country=models.ForeignKey(
        Country, on_delete=models.CASCADE)
	district=models.CharField(max_length=13)
	prime=models.BooleanField(default=False)
	advance_prime=models.BooleanField(default=False)
	advertisers=models.BooleanField(default=False)
	date_added =models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.username
    
class Watched_Total_Price(models.Model):
	person = models.ForeignKey(
        User, on_delete=models.CASCADE)
	total_ads_money = models.CharField(max_length = 30)
	date_watched =models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.person

	class Meta:
		ordering = ('-date_watched', )


class Watched_Total(models.Model):
	person = models.ForeignKey(
        User, on_delete=models.CASCADE)
	total_ads_watched = models.CharField(max_length = 30)
	date_watched =models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.person

	class Meta:
		ordering = ('-date_watched', )

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



class Ad(models.Model):
	file = models.FileField(blank=True,null=True)
	description_of_ad= models.TextField()
	button_link= models.CharField(max_length=1000)
	videolink = models.CharField(max_length=1000,blank=True,null=True)
	location = models.ForeignKey(
        Location, on_delete=models.CASCADE)
	prime_price_per_click =  models.IntegerField(default=0.26)
	advance_prime_price_per_click =  models.IntegerField(default=0.45)
	
	@staticmethod
	def get_ads_by_id(ids):
		return Ad.objects.filter(id__in =ids).order_by('-id')
	@staticmethod
	def get_ad_by_id(id):
		return Ad.objects.filter(id__in =id).order_by('?')




	def __str__(self):
		return self.location



class Billing_rave(models.Model):
	customer=models.ForeignKey(
        User, on_delete=models.CASCADE)
	amount=models.PositiveIntegerField()
	currency=models.CharField(max_length=200)
	reference=models.CharField(max_length=200)
	email=models.EmailField()
	phone_no=models.CharField(max_length=200)
	verified=models.BooleanField(default=False)
	transaction_id=models.CharField(max_length=2000)
	Completed_status=models.BooleanField(default=True)
	date_created=models.DateTimeField(auto_now_add=True)
