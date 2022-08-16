from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User

def group_check_prime_user(user):
    return user.groups.filter(name__in=['Prime_User'])

def group_check_advance_prime_user(user):
    return user.groups.filter(name__in=['Advance_Prime_User'])

# Create your views here.
def index(request):
    context={}
    return render(request,'documentation.html',context)
def billing(request):
    user=User.object.filter(id=request.user.id)
    
    return render(request,'billing.html',{})

def profile(request):
    if request.user.is_authenticated:
        user=User.object.filter(id=request.user.id)
    else:
        user=None
    context={'user':user}
    return render(request,'profile.html',context)
def signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username,password=password)

        if user is not None:
            login(request,user)
            request.session['customer'] = user.id
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            else:
                messages.success(request, f'Welcome, {username}.You have Signed In Successfully')
                return redirect('dashboard')
        else:
            messages.success(request, 'Username or Password Incorrect!')
            context={}
            return render(request,'sign-in.html',context)
    context={}
    return render(request,'sign-in.html',context)
def signup(response):
    if response.method=="POST":
        form=RegistrationForm(response.POST)
        if form.is_valid():
            if User.objects.filter(email=form.cleaned_data['email']):
                messages.success(response, f'Email already in use, Please use a different Email')
                return render(response,'signup.html',)
            elif User.objects.filter(username=form.cleaned_data['username']):
                messages.success(response, f'Username already in use, Please use a different Username')
                return render(response,'signup.html',)
            form.save()
            messages.success(response, f'Successfully Registered,Please log into your Account to Make Orders')
            return redirect('login')
    else:
        form=RegistrationForm()
    context={'form':form}
    return render(request,'sign-up.html',context)
def tables(request):
    watched=Watched.object.filter(person=request.user)
    context={'watched':watched}
    return render(request,'tables.html',context)
def dashboard(request):
    ades=Ads.object.filter(prime=False)
    watched=Watched.object.filter(ids=request.user.id)
    ads={}
    for ad in ades:
        if ad not in watched:
            ads.append(ad)
    newads=ads[0]
    context={'newads':newads}
    return render(request,'dashboard.html',context)

def Primeuser(request):
    ades=Ads.object.filter(prime=True)
    watched=Watched.object.filter(ids=request.user.id)
    ads={}
    for ad in ades:
        if ad not in watched:
            ads.append(ad)
    newads=ads[0]
    context={'newads':newads}
    return render(request,'dashboard.html',context)
def become_prime_user(request):
    try:
        prime_group = Group.objects.get(name = 'Prime_User')
    except:
        prime_group_created= Group.objects.create(name='Prime_User')
        prime_group = Group.objects.get(name = 'Prime_User')
    user=User.objects.get(id=request.user.id)
    user.groups.add(prime_group)
    return render(request,'dashboard.html',context)

def become_advance_prime_user(request):
    try:
        prime_group = Group.objects.get(name = 'Advance_Prime_User')
    except:
        prime_group_created= Group.objects.create(name='Advance_Prime_User')
        prime_group = Group.objects.get(name = 'Advance_Prime_User')
    user=User.objects.get(id=request.user.id)
    user.groups.add(prime_group)
    return render(request,'dashboard.html',context)

