from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

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
            return redirect('home')
        else:
            messages.info(request,'username OR password in incorrect')
            return render(request,'login.html')


    return render(request,'login.html')



def logout_view(request):
    logout(request)
    messages.warning(request,'your logged out')
    return redirect('login')



def home(request):
    return render(request,'travel_home.html')