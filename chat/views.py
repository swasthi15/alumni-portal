from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

def index(request):
    return render(request, 'index2.html', {})

def room(request, room_name):
    return render(request, 'room1.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'username':request.user
    })