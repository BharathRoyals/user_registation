from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse
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
            return HttpResponse('insert the data successfully')
        else:
            return HttpResponse('Data not valid')




    return render(request,'registrations.html',d)