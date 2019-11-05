from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
#from . import templates
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import auth
from events.models import events

def index(request):
	eventlist = events.objects.all()
	print(eventlist)
	return render(request,'events/templates/index.html',{'eventlist':eventlist})

def create_event(request):
    title = request.POST.get('title')
    date = request.POST.get('date')
    description = request.POST.get('description')
    organizer = request.POST.get('organizer')
    department = request.POST.get('department')
    
    new_event = events.objects.create(title=title,date=date,description=description,image='',user=request.user,organizer=organizer,department=department)
    new_event.save()
    print(title,date,description)
    return HttpResponse('shortcuts')

def event_detail(request,event_id):
	
	print(event_id)
	event_obj = events.objects.get(id=event_id)
	print(event_obj.description)
	return render(request,'events/templates/eventdetail.html',{'event_obj':event_obj})