from django.db import models

# title
# date
# time of event
# description
# image
from django.contrib.auth.models import User


class events(models.Model):

    title = models.CharField(max_length=100, null=False,default=None)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.CharField(max_length=100, null=False,default=None)
    description =  models.CharField(max_length=2000, null=True,default=None)
    image = models.CharField(max_length=100,null=True,default=None)
    organizer = models.CharField(max_length=100,null=True,default=None)
    department = models.CharField(max_length=100,null=True,default=None)
   