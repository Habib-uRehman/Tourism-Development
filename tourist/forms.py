from dataclasses import fields
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import touristguideform


class Touristguideform(ModelForm):
    class Meta:
        model = touristguideform
        fields = '__all__'