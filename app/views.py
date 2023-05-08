from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse
from django.core.mail import send_mail
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