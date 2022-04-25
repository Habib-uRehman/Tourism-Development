from dataclasses import fields
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import restraunt


class RestrauntForm(ModelForm):
    class Meta:
        model = restraunt
        fields = '__all__'
        




