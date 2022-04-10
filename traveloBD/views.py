from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Dist_info,Tour_places,Gallery_photos,PopulerPlaces

from .forms import CreateUserForm
# Create your views here.
def registration_view(request):
    form = CreateUserForm()
    if request.method == "POST":
        form =CreateUserForm(request.POST)
    if form.is_valid():
        form.save()
        user=form.cleaned_data.get('username')
        messages.success(request,'Account Was created for '+ user)
        return redirect('login')
    context = {
        'form' : form
    }
    return render(request,'registration.html',context)






def login_view(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home_page')
        else:
            messages.info(request,'username OR password in incorrect')
            return render(request,'login.html')


    return render(request,'login.html')



def logout_view(request):
    logout(request)
    messages.warning(request,'Logged out')
    return redirect('login')



def home(request):
    dests=Dist_info.objects.all()
    return render(request,'travel_home.html',{'dests':dests})


def about_view(request):
    return render(request,'siteinfo/about.html',{'about':about_view})

def contact_view(request):
    return render(request,'siteinfo/contact.html',{'contact':contact_view})

def gallery_view(request):
    photos=Gallery_photos.objects.all()
    populer_photo_details=PopulerPlaces.objects.all()
    context={
        'g_photos': photos,
        'p_photos':populer_photo_details
    }
    return render(request,'siteinfo/gallery.html',context)



def places_info(request,id=None):
    place=[]

    if id is not None:
        name=Dist_info.objects.get(id=id)

        place=Tour_places.objects.filter(dist_info=name)

    context={

        'district_name':name,
        'place': place
    }
    return render(request,'places/places.html',context)



def spots_view(request,id):
    place = Tour_places.objects.get(id=id)
    context={
        'place':place
    }
    return render(request,'places/spots.html',context)


def bus_ticket(request):
    obj=Tour_places.objects.all()
    context={
        'obj':obj
    }
    return render(request,'ticket/bus.html',context)


def train_ticket(request):
    obj = Tour_places.objects.all()
    context = {
        'obj': obj
    }
    return render(request,'ticket/train.html',context)


def flight_ticket(request):
    obj = Tour_places.objects.all()
    context = {
        'obj': obj
    }
    return render(request,'ticket/flight.html',context)
