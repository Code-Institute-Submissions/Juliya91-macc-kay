from django import forms
from .models import Capture, Artist


class CaptureForm(forms.ModelForm):

    class Meta:
        model = Capture
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        artists = Artist.objects.all()
        friendly_names = [(a.id, a.get_friendly_name()) for a in artists]

        self.fields['artist'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'