from django.shortcuts import render

# Create your views here.
def log_reg(request):
    return render(request,'login and reg.html')


def logout_view(request):
    return render(request,'log out.html')