
from django import forms
from django.forms.models import inlineformset_factory

from .models import Author, Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = (
            'title',
            'number_of_pages'
        )
