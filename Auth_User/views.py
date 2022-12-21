from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Create your views here.


def User_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('Login success!')
        else:
            messages.error(request, 'Username and password not same!')
            return redirect('Login:login')
        
    context = {
        
    }
    return render(request, 'Auth_User/login.html', context)


def User_Registration(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        usernamee = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if User.objects.filter(username=usernamee).exists():
            messages.warning(request, 'Username Already Exist!')
            return redirect('Login:registration')
        else:
            if password1 == password2:
                user = User(first_name=first_name, last_name=last_name, username=usernamee, email=email)
                user.set_password(password1)
                user.save()
                messages.success(request, 'Account Create Successfull!')
                return redirect('Login:login')
            else:
                messages.warning(request, 'Password Not match')
                return redirect('Login:registration')
                    
                    
     
     
     
     
     
    context = {
        
    }
    return render(request, 'Auth_User/Registration.html', context)


