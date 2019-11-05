from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('create_event/',views.create_event),
    path('<int:event_id>/',views.event_detail)
    
]
