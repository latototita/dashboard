from django.shortcuts import render
from django.contrib import messages
from Main.models import *
from Main.forms import *

# Create your views here.
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
        form=CustomUserCreationForm(response.POST)
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
        form=CustomUserCreationForm()
    context={'form':form}
    return render(response,'sign-up.html',context)