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
	return render(request,'alumni_portal/templates/home.html',{'user':request.user})