from django import forms
from .models import Tour


class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ('first_name', 'last_name',
                  'email', 'preferred_time',)
