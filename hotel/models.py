import datetime
import numbers
from django.db import models
from pyexpat import model
from django.contrib.auth.models import AbstractBaseUser
from django.forms import CharField, DateField
from multiselectfield import MultiSelectField


class HotelRegistration(models.Model):

    hotel_name = models.CharField(max_length=100) # Name of the hotel



    def __str__(self):
        return self.hotel_name
 


 


