from django import forms
from .models import Tour
from django.forms import ModelForm


class DateInput(forms.DateInput):
    input_type = 'date'


class TourForm(forms.ModelForm):

    class Meta:
        model = Tour
        fields = ('first_name', 'last_name', 'email',
                  'preferred_time', 'preferred_date',)
        widgets = {
            'preferred_date': DateInput(),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email Address'}),
        }
        labels = {
            "first_name": "",
            "last_name": "",
            "email": "",
        }
