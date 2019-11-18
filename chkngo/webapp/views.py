from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.
def RestoList(request):
    resto_list = Restaurant.objects.all()
    context = {'resto_list': resto_list}
    return render(request, 'resto_list.html', context)

def RestoView(request, RestoID):
    resto_deets = Restaurant.objects.get(RestoID = RestoID)
    context = {'resto_deets': resto_deets}
    return render(request, 'restoView.html', context)

def ReviewUpload(request, RestoID):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            ReviewObj = Review()
            ReviewObj.RestoID = Restaurant.objects.get(RestoID = RestoID)
            ReviewObj.Rating = form.cleaned_data.get('Rating')
            ReviewObj.save()
            #Update Restaurant Review Average
            Resto = Restaurant.objects.get(RestoID = RestoID)
            AllRatings = Review.objects.filter(RestoID = RestoID)
            AveRate = 0
            RateCount = 0
            for x in AllRatings:
                AveRate = AveRate + x.Rating
                RateCount += 1
            AveRate = AveRate / RateCount #AVerage Rating for Restaurant
            Resto.Rating = AveRate
            Resto.save(force_update = True)
        return redirect('RestoList')
    else:
        form = ReviewForm()
        context= {'form':form}
        return render (request, 'review_upload.html', context)

def Register(request):
    if request.method =="POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account Created for {username}! go ahead and log in!')
            return redirect('Register')
    else:
        form = RegistrationForm()
    context = {'form':form}
    return render(request,'registration_page.html',context)

