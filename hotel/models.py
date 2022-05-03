from django.db import models

# Create your models here.
import datetime
import numbers
from django.db import models
from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.forms import CharField, DateField
from multiselectfield import MultiSelectField


class HotelRegistration(models.Model):

    hotel_name = models.CharField(max_length=100) # Name of the hotel
    establishment_year = models.DateField(default=datetime.date.today) # year of establishment
    commision_date = models.DateField(default=datetime.date.today) # data of commission    
    telex_number = models.CharField(max_length=100) # Telex number
    phone_number = models.CharField(max_length=100)# Telephone Number
    hotel_address = models.CharField(max_length=100) # Address
    telegraphic_address = models.CharField(max_length=100) # Telegraphic Address


 


