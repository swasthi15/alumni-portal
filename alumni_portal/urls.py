"""alumni_portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from events import urls as events_urls
from chat import urls as chat_urls
from django.conf.urls.static import  static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index),
    path('chat/', include(chat_urls)),
    path('signup/',views.signup),
    path('signup_submit/',views.signup_submit),
    path('login/',views.login),
    path('logging_in/',views.logging_in),
    path('logout/',views.logout),
    path('events/',include(events_urls))
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
