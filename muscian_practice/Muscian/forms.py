from django import forms
from .models import Musician
type= [('Guiter','guiter'),('Piano','piano'),('Violin','violin'),('Drum','drum')]
class MusicianForm(forms.ModelForm):
    Instrument_type = forms.ChoiceField(choices=type)
    class Meta:
        model = Musician
        fields = '__all__'
        