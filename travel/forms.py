from dataclasses import fields
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import travelagency


class travelagencyform(ModelForm):
    class Meta:
        model = travelagency
        fields = '__all__'
        