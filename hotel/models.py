import datetime
import numbers
from django.db import models
from pyexpat import model
from django.contrib.auth.models import AbstractBaseUser
from django.forms import CharField, DateField
from multiselectfield import MultiSelectField


class HotelRegistration(models.Model):

    hotel_name = models.CharField(max_length=100 , null=True) # Name of the hotel
    establishment_year = models.DateField(default=datetime.date.today , null=True) # year of establishment
    commision_date = models.DateField(default=datetime.date.today , null=True) # data of commission    
    telex_number = models.CharField(max_length=100 , null=True) # Telex number
    phone_number = models.CharField(max_length=100 , null=True)# Telephone Number
    hotel_address = models.CharField(max_length=100 , null=True) # Address
    telegraphic_address = models.CharField(max_length=100 , null=True) # Telegraphic Address




    def __str__(self):
        return self.hotel_name
 


 


