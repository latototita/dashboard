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
from django.views import View

def group_check_prime_user(user):
    return user.groups.filter(name__in=['Prime_User'])

def group_check_advance_prime_user(user):
    return user.groups.filter(name__in=['Advance_Prime_User'])

# Create your views here.
def index(request):
    context={}
    return render(request,'documentation.html',context)
def billing(request):
    result = request.GET.get('result', None)
    if request.method=='POST':
        if result.status=="successful":
            billing=Billing_rave(
                customer=request.user,
                amount=result.amount,
                currency=result.currency,
                reference=result.tx_ref,
                email=result.email,
                phone_no=result.phoneNumber,
                transaction_id=result.transaction_id,
                )
            billing.save()
            messages.success(request, f'Payment successful, Amount: {result.amount} {result.currency} Paid with a transaction ID of {result.transaction_id}')
            return redirect('billing')
        if result.status!="successful":
            messages.success(request, 'Error Making Payments, Payment Failed. Check Your Finances')
            return redirect('billing')
    if request.user.is_authenticated:
        user=request.user
    else:
        user=None
    context={'user':user}
    return render(request,'billing.html',context)

def profile(request):
    busket = request.session.get('busket')
    if not busket:
        request.session['busket'] = {}
        ades={}
    else:
        ades = Ad.get_ads_by_id(list(request.session.get('busket').keys()))
    if request.user.is_authenticated:
        user=User.objects.filter(id=request.user.id)
    else:
        user=None
    if request.user.is_authenticated:
        try:
            ades=Ad.objects.filter()
        except:
            ades={}
        try:
            watched=Watched.objects.filter(ids=request.user.id)
        except:
            watched={}
        ads={}
        if ades is not {} and watched is not {}:
            for ad in ades:
                if ad not in watched:
                    ads.append(ad)
                newads=ads[0]
    else:
        newads=None
    if request.user.prime==True:
    elif request.user.advance_prime==True:
    elif request.user.advertiser==True:
    else:
    context={'user':user,'newads':newads,}
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
    if request.method=="POST":
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
    return render(request,'Form.html',context)

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
    return render(request,'Form.html',context)

class Busket(View):

    def post(self , request):
        ad = request.POST.get('ad')
        busket = request.session.get('busket')
        if busket:
            quantity = busket.get(ad)
            if quantity:
                if remove:
                    if quantity<=1:
                        busket.pop(ad)
                    else:
                        busket[ad]  = quantity-1
                else:
                    busket[ad]  = quantity+1

            else:
                busket[ad] = 1
        else:
            busket = {}
            busket[ad] = 1

        request.session['busket'] = busket
        return redirect('profile')



    def get(self , request):
        # print()
        return HttpResponseRedirect(f'/profile{request.get_full_path()[1:]}')
