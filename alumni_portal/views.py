from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import templates
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import auth

def index(request):
	print(request.user)
	print("Hitting Home Page Successfull")

	#return HttpResponse("Done and dusted")
	return render(request,'alumni_portal/templates/home1.html',{'user':request.user})

def signup(request):
	print("signup")
	return render(request,'alumni_portal/templates/signup1.html')

def signup_submit(request):
	
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    last_name = request.POST.get('number')
    usertype = request.POST.get('type')
    print(usertype)
    if usertype=='student' :
    	user = User.objects.create_user(username, email,password,is_staff=True,last_name=last_name )
    else:
    	user = User.objects.create_user(username, email,password,is_staff=False,last_name=last_name )
    user.save()

    return redirect('/login')

	
def login(request):
	print(request.user)

	#return HttpResponse("Done and dusted")
	return render(request,'alumni_portal/templates/login.html')

def logging_in(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    print(user)
    print("login")
    if user is not None:
        auth.login(request,user)
        print("Successfull")
        print(username)
        return redirect('/')
        # Redirect to a success page.
        ...
    else:
        return redirect('/')

def logout(request):
    auth.logout(request)
    return redirect('/')