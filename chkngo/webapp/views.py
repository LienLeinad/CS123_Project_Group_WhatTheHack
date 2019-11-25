from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages
import uuid
from django.contrib.auth.decorators import login_required

#A simple mean Average Algorithm, input must be a list of a certain element, outputs integer mean
def average(list):
    AveNum = 0
    AveCount = 0
    for x in list:
        AveNum += x.Rating
        AveCount += 1
    AveNum = AveNum / AveCount
    return AveNum



# Create your views here.
# def Home(request):

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
            ReviewObj.ReviewID = uuid.uuid1()
            ReviewObj.RestoID = Restaurant.objects.get(RestoID = RestoID)
            ReviewObj.Rating = form.cleaned_data.get('Rating')
            ReviewObj.save()
            #Update Restaurant Review Average
            Resto = Restaurant.objects.get(RestoID = RestoID)
            AllRatings = Review.objects.filter(RestoID = RestoID)
            AveRate = average(AllRatings)
            Resto.Rating = AveRate
            Resto.save(force_update = True)
        return redirect('RestoView', RestoID = RestoID)
    else:
        form = ReviewForm()
        context= {'form':form}
        return render (request, 'review_upload.html', context)

def Register(request):
    if request.method =="POST":
        form = RegistrationForm(request.POST)
        form2 = RMRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            temp_user = CustomUser.objects.get(username = username)
            if form.cleaned_data.get('user_type') == 'RM':
                if form2.is_valid():
                    opTime = form2.cleaned_data.get('Open_time')
                    clTime = form2.cleaned_data.get('Closing_time')
                    Add = form2.cleaned_data.get('Address')
                    Land = form2.cleaned_data.get('Landline')
                    Cont = form2.cleaned_data.get('Contact')
                    temp_Res = Restaurant(RestoID = form2.cleaned_data.get('RestoID'),
                                        MngID = temp_user,
                                        Open_time = opTime,
                                        Closing_time = clTime,
                                        Address = Add,
                                        Landline = Land,
                                        Contact = Cont
                                        )
                    temp_Res.save()
           
            messages.success(request,f'Account Created for {username}! go ahead and log in!')
            return redirect('Register')
    else:
        form = RegistrationForm()
        form2 = RMRegistrationForm()
    context = {'form':form,'form2':form2}
    return render(request,'registration_page.html',context)

def MakeCategory(request):
    if(request.method == "POST"):
        form = CategoryForm(request.POST)
        if form.is_valid():
            tempCat = Categories()
            tempCat.CatID = uuid.uuid1()
            tempCat.CatName = form.cleaned_data.get('CatName')
            tempCat.save()
            return redirect('Register')
    else:
        form = CategoryForm()
    context = {'form':form}
    return render(request,'make_category.html',context)

def RestaurantManagement(request,RestoID):
    if not request.user.is_authenticated and not request.user.user_type == 'RM':
        return redirect('RestoView',RestoID = RestoID)
        print("NOT AUTHENTICATED USER")
    if request.method == 'POST':
        form = RestoEditForm(data = request.POST)
        temp_resto = Restaurant.objects.get(RestoID = RestoID)
        if form.is_valid():
            if form.cleaned_data.get('Open_time') == None:
                print("Nothing change Open_time")
            else:
                temp_resto.Open_time = form.cleaned_data.get('Open_time')
            if form.cleaned_data.get('Closing_time') == None:
                print("Nothing change Closing_time")
            else:
                temp_resto.Closing_time = form.cleaned_data.get('Closing_time')
            if form.cleaned_data.get('Address') == '':
                print("Nothing change Address")
            else:
                temp_resto.Address = form.cleaned_data.get('Address')
            if form.cleaned_data.get('Landline') == '':
                print("Nothing change Landline")
            else:
                temp_resto.Landline = form.cleaned_data.get('Landline')
            if form.cleaned_data.get('Contact') == '':
                print("Nothing change Contact")
            else:
                temp_resto.Contact = form.cleaned_data.get('Contact')
            temp_resto.save(force_update = True)
            return redirect('RestoView', RestoID = RestoID)
    else:
        form = RestoEditForm()
    context = {'form':form}
    return render(request, 'restaurant_management.html',context)