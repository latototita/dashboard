from django.shortcuts import render

# Create your views here.
def index(request):
    context={}
    return render(request,'documentation.html',context)
def billing(request):
    return render(request,'billing.html',{})

def profile(request):
    context={}
    return render(request,'profile.html',context)
def signup(request):
    return render(request,'sign-up.html',{})
def signin(request):
    return render(request,'sign-in.html',{})
def tables(request):
    return render(request,'tables.html',{})
def dashboard(request):
    return render(request,'dashboard.html',{})

