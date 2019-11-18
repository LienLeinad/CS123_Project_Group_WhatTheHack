from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.
def RestoList(request):
    resto_list = Restaurant.objects.all()
    context = {'resto_list': resto_list}
    return render(request, 'resto_list.html', context)

def RestoView(request, RestaurantID):
    resto_deets = Restaurant.objects.get(RestaurantID = RestaurantID)
    context = {'resto_deets': resto_deets}
    return render(request, 'restoView.html', context)

def ReviewUpload(request, RestaurantID):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            ReviewObj = Review()
            ReviewObj.RestaurantID = Restaurant.objects.get(RestaurantID = RestaurantID)
            ReviewObj.Rating = form.cleaned_data.get('Rating')
            ReviewObj.save()
            #Update Restaurant Review Average
            Resto = Restaurant.objects.get(RestaurantID = RestaurantID)
            AllRatings = Review.objects.filter(RestaurantID = RestaurantID)
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