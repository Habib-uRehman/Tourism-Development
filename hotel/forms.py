from dataclasses import fields
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import HotelRegistration


class HotelForm(ModelForm):
    class Meta:
        model = HotelRegistration
        fields = '__all__'