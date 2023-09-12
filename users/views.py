from django.shortcuts import redirect, render

from users.forms import FormLoginUser
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.


def login_user(request):
    
    
    
    if request.method =='POST':
        name=request.POST['username']
        password=request.POST['password']
        
        
        user = authenticate(request,username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('login')
        
        
    return render(request,'auth/login.html')




def signup(request):
    
    
    if request.method =='POST':
        name=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        
        
        if password1==password2: 
             messages.error(request, "Passwords didn't matched!!")
             
             if User.objects.filter(email=email).exists() :
                 messages.error(request, "Email Already Registered!!")
             else:
                 
                 user = User.objects.create_user(name, email, password1)    
                 user.save()
                 login(request, user)
                 return redirect('home')
             
    return render(request,'auth/signup.html')



def logout_user(request):
    logout(request)
    return redirect('home')