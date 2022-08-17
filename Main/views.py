from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *

def group_check_prime_user(user):
    return user.groups.filter(name__in=['Prime_User'])

def group_check_advance_prime_user(user):
    return user.groups.filter(name__in=['Advance_Prime_User'])

# Create your views here.
def index(request):
    context={}
    return render(request,'documentation.html',context)
def billing(request):
    if request.user.is_authenticated:
        user=User.objects.filter(id=request.user.id)
    
    return render(request,'billing.html',{})

def profile(request):
    if request.user.is_authenticated:
        user=User.objects.filter(id=request.user.id)
    else:
        user=None
    context={'user':user}
    return render(request,'profile.html',context)

def tables(request):
    if request.user.is_authenticated:
        watched=Watched.objects.filter(person=request.user)
    else:
        watched=None
    context={'watched':watched}
    return render(request,'tables.html',context)
def dashboard(request):
    if request.user.is_authenticated:
        watched=Watched.objects.filter(ids=request.user.id)
        ads={}
        for ad in ades:
            if ad not in watched:
                ads.append(ad)
            newads=ads[0]
    else:
        newads=None
    context={'newads':newads}
    return render(request,'dashboard.html',context)

def Primeuser(request):
    ades=Ads.objects.filter(prime=True)
    watched=Watched.objects.filter(ids=request.user.id)
    ads={}
    for ad in ades:
        if ad not in watched:
            ads.append(ad)
    newads=ads[0]
    context={'newads':newads}
    return render(request,'dashboard.html',context)
def become_prime_user(request):
    if response.method=="POST":
        form = Join_Prime_Form(request.POST, request.FILES)
        if form.is_valid():
            try:
                prime_group = Group.objects.get(name = 'Prime_User')
            except:
                prime_group_created= Group.objects.create(name='Prime_User')
                prime_group = Group.objects.get(name = 'Prime_User')
            user=User.objects.get(id=request.user.id)
            user.groups.add(prime_group)
            form.save()
    else:
        form = Join_Prime_Form()
        context={'form':form}
    return render(request,'dashboard.html',context)

def become_advance_prime_user(request):
    if response.method=="POST":
        form = Join_Advance_Prime_Form(request.POST, request.FILES)
        if form.is_valid():
            try:
                prime_group = Group.objects.get(name = 'Advance_Prime_User')
            except:
                prime_group_created= Group.objects.create(name='Advance_Prime_User')
                prime_group = Group.objects.get(name = 'Advance_Prime_User')
            user=User.objects.get(id=request.user.id)
            user.groups.add(prime_group)
            form.save()
    else:
        form = Join_Advance_Prime_Form()
        context={'form':form}
    return render(request,'dashboard.html',context)

