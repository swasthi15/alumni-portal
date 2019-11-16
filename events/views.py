from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
#from . import templates
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import auth
from events.models import events
from django.core.files.storage import FileSystemStorage
from django.conf import settings

def index(request):
	eventlist = events.objects.all()
	print(eventlist)
	return render(request,'events/templates/eventlist.html',{'eventlist':eventlist})

def create_event(request):
    return render(request,'events/templates/create_event.html',{'user':request.user})

def create_event_submit(request):
    title = request.POST.get('title')
    date = request.POST.get('date')
    description = request.POST.get('description')
    organizer = request.POST.get('organizer')
    department = request.POST.get('department')
    if request.method == 'POST' and request.FILES['myfile1']:
        
        myfile = request.FILES['myfile1']
        print(myfile)
        fs = FileSystemStorage()
        name = title + "-" + date + "-" + organizer + "-" + department+"-" + myfile.name
        filename = fs.save(name, myfile)
        uploaded_file_url = fs.url(filename)
        print(uploaded_file_url)
    new_event = events.objects.create(title=title,date=date,description=description,image=name,user=request.user,organizer=organizer,department=department)
    new_event.save()
    print(title,date,description)

    eventlist = events.objects.all()
    return redirect('/events')


def event_detail(request,event_id):
	
	print(event_id)
	event_obj = events.objects.get(id=event_id)
	print(event_obj.description)
	return render(request,'events/templates/eventdetail.html',{'event_obj':event_obj})

def alumnilist(request):
    usertype = User.objects.filter(is_staff=0)
    print(usertype)