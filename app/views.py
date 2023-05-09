from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
def home(request):
    if request.session.get('username'):
        username=request.session.get('username')
        d={'username':username}
        return render(request,'home.html',d)

    return render(request,'home.html')


def registrations(request):
    UFO=UserForm()
    PFO=ProfileForm()
    d={'UFO':UFO,'PFO':PFO}


    if request.method=='POST' and request.FILES:
        UFD=UserForm(request.POST)
        PFD=ProfileForm(request.POST,request.FILES)
        if UFD.is_valid() and PFD.is_valid():
        
            Chintu=UFD.save(commit=False)
            Chintu.set_password(UFD.cleaned_data['password'])
        
            Chintu.save()


            Chamu=PFD.save(commit=False)
            Chamu.username=Chintu
            Chamu.save()


            send_mail('Enter your Account Details',
                    'your account can be hacked',
                    'bharathp0327@gmail.com',
                    [Chintu.email],
                    fail_silently=True)
            return HttpResponse('insert the data successfully')
        else:
        
            return HttpResponse('Data not valid')




    return render(request,'registrations.html',d)


def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        AUO=authenticate(username=username,password=password)
        if AUO and AUO.is_active:
            login(request,AUO)
            request.session['username']=username
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse('Invalid username or password')
        
    return render(request,'user_login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
def display_profile(request):
    username=request.session.get('username')
    UO=User.objects.get(username=username)
    PO=profile.objects.get(username=UO)
    d={'UO':UO,'PO':PO}



    return render(request,'display_profile.html',d)

@login_required
def change_password(request):
    if request.method=='POST':
        password=request.POST['pw']
        username=request.session.get('username')
        UO=User.objects.get(username=username)
        UO.set_password(password)
        UO.save()
        return HttpResponse('insert  change the password successfully')
    return render(request,'change_password.html')

def forget_password(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['pw']
    
        UO=User.objects.get(username=username)
        UO.set_password(password)
        UO.save()
        return HttpResponse('insert the password successfully')
    return render(request,'forget_password.html')