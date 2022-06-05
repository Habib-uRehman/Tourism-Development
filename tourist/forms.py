from dataclasses import fields
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import touristguideform


class Touristguideform(forms.ModelForm):
    class Meta:
        model = touristguideform
        # fields = '__all__'
        fields = ('guide_name' , 'business_address' )