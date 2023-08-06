from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from  django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
@login_required(login_url="login")
def Homepage(request):
    return render(request,"home.html")

def Login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('pass')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("start")
        else:
            return HttpResponse("user name or password is incorrect!!!!")

    return render(request,"login.html")

def signup(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("password is not matching")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect("login")

       
    return render(request,"signup.html")

def Logout(request):
    logout(request)
    return redirect("login")


# Create your views here.
