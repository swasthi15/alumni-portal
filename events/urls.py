from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('create_event/',views.create_event),
    path('create_event_submit/',views.create_event_submit),
    path('<int:event_id>/',views.event_detail)
    
]
