from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages
import uuid
import datetime,statistics
from django.db.models import Q

#A simple mean Average Algorithm, input must be a list of a certain element, outputs integer mean
def average(list):
    AveNum = 0
    AveCount = 0
    for x in list:
        AveNum += x.Rating
        AveCount += 1
    AveNum = AveNum / AveCount
    return AveNum

#Mode Algorithm given queryset of waitlistentries





#Mode average function using statistics
# def mode(list):
#     try:
#         return statistics.mode(list)
#     except:
#         return statistics.mean(list)


# Create your views here.
# def Home(request):
# def SeeWaitlist(request, RestoID):
#     if request.method == 'POST':
#         form = WaitListEntryForm(request.POST)
#         if form.is_valid():
#             temp_WLE= WaitListEntry(RestoID = Restaurant.objects.get(RestoID = RestoID),
#                                     first_name = form.cleaned_data.get('first_name'),
#                                     last_name = form.cleaned_data.get('last_name'),
#                                     PaxCount = form.cleaned_data.get('PaxCount'))
#             temp_WLE.save()
#             return redirect('RestoView', RestoID = RestoID)
#     else:
#         form = WaitListEntryForm() 
#     context = {'form': form}
#     return render(request,'wait_list.html',context)


def LandingPage(request):
    category_list = Categories.objects.values('CatName')
    context = {'category_list': category_list}
    return render(request, 'landingPage.html', context)

def RestoList(request):
    resto_list = Restaurant.objects.all()
    context = {'resto_list': resto_list}
    return render(request, 'resto_list.html', context)

def RestoView(request, RestoID):
    resto_deets = Restaurant.objects.get(RestoID = RestoID)
    WaitList = WaitListEntry.objects.filter(RestoID = RestoID,
                                            # Seated = False
                                            )
    if request.method == 'POST':
        form = WaitListEntryForm(request.POST)
        if form.is_valid():
            temp_WLE= WaitListEntry(RestoID = Restaurant.objects.get(RestoID = RestoID),
                                    first_name = form.cleaned_data.get('first_name'),
                                    last_name = form.cleaned_data.get('last_name'),
                                    PaxCount = form.cleaned_data.get('PaxCount'))
            temp_WLE.save()
            return redirect('RestoView', RestoID = RestoID)
    else:
        form = WaitListEntryForm() 
    # context = {}
    context = {'resto_deets': resto_deets, 'WaitList':WaitList, 'user':request.user,'form': form}
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
            print(form.cleaned_data.get('user_type'))
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
                    print(temp_Res)
                    temp_Res.save()
                    print(Restaurant.objects.all())
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
    if not request.user.user_type == "RM" or (request.user.is_authenticated and not Restaurant.objects.get(RestoID = RestoID).MngID == request.user):
        messages.success(request,'page you\'re tryring to access is forbidden')
        return redirect('RestoList')
    elif request.method == 'POST':
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

def DeleteEntry(request,RestoID,first_name,last_name,id):
    WaitListEntry.objects.filter(id = id,first_name = first_name, last_name = last_name, RestoID = Restaurant.objects.get(RestoID = RestoID)).delete()
    return redirect('RestoView', RestoID = RestoID)

def SeatEntry(request,RestoID,id):
    RestoWait = Restaurant.objects.get(RestoID = RestoID)
    seatedEntry = WaitListEntry.objects.get(id = id)
    seatedEntry.Seated = True
    seatedEntry.save() #to add time seated to the attributes too
    time_waited = (seatedEntry.TimeOut - seatedEntry.TimeIn).total_seconds()//60
    seatedEntry.WaitTime = time_waited
    seatedEntry.save()
    #fix the average of the restaurant
    if seatedEntry.PaxCount >=  9 and seatedEntry.PaxCount <= 12:
        # print(statistics.mode(WaitListEntry.objects.exclude(Seated = False, WaitTime = None).filter(PaxCount__lte = 12, PaxCount__gte = 9,Seated = True).values_list('WaitTime',flat = True)))
        try:
            RestoWait.WaitTime9_12 = statistics.mode(WaitListEntry.objects.exclude(WaitTime = None, Seatead = False).filter(PaxCount__lte = 12, PaxCount__gte = 9).values_list('WaitTime',flat = True))
        except:
            RestoWait.WaitTime9_12 = statistics.mean(WaitListEntry.objects.filter(PaxCount__lte = 12, PaxCount__gte = 9).values_list('WaitTime',flat = True))
    elif seatedEntry.PaxCount >= 5 and seatedEntry.PaxCount <= 8:
        try:
            RestoWait.WaitTime5_8 = statistics.mode(WaitListEntry.objects.filter(PaxCount__lte = 8, PaxCount__gte = 5).values_list('WaitTime',flat = True))
        except:
            RestoWait.WaitTime5_8 = statistics.mean(WaitListEntry.objects.filter(PaxCount__lte = 8, PaxCount__gte = 5).values_list('WaitTime',flat = True))
        # print( mode(WaitListEntry.objects.filter(PaxCount__lte = 8, PaxCount__gte = 5).WaitTime))
    elif seatedEntry.PaxCount <= 4 and seatedEntry.PaxCount >= 1:
        try:
            RestoWait.WaitTime1_4 = statistics.mode(WaitListEntry.objects.filter(PaxCount__lte = 4, PaxCount__gte = 1).values_list('WaitTime',flat = True))
        except:
            RestoWait.WaitTime1_4 = statistics.mean(WaitListEntry.objects.filter(PaxCount__lte = 4, PaxCount__gte = 1).values_list('WaitTime',flat = True))
        # print(mode(WaitListEntry.objects.filter(PaxCount__lte = 4, PaxCount__gte = 1).WaitTime))
    seatedEntry.save()
    RestoWait.save()
    return redirect('RestoView',RestoID = RestoID)

# IMPORTANT: NOT A VIEW TO SEE THE WAIT LIST ANYMORE, JUST A TEST VIEW FOR ADDING WAITLIST ENTRIES BEFORE THE FRONT END GETS INTEGRATED TO RESTOVIEW

#Q(RestoID__icontains=query) | 
#search
def searchposts(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')
        if query is not None:
            res=Restaurant.objects.all()
            tmp = Q(CatName__icontains=query)
            cats=Categories.objects.filter(tmp).distinct()
            print(cats)
            lookups=Q()

            for cn in cats:
                for rr in cn.Restaurants.all():
                    print(rr.RestoID)
                    lookups = lookups | Q(RestoID = rr.RestoID)
            lookups= lookups | Q(RestoID__icontains=query)
            print(lookups)

            results= Restaurant.objects.filter(lookups).distinct()
            print(results)
            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'search.html', context)

        else:
            return render(request, 'search.html')

    else:
        return render(request, 'search.html')
