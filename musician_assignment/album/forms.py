from django import forms
from .models import Album
numbers = [('1', '1'), ('2', '2'), ('3','3'), ('4', '4'), ('5', '5')]
class AlbumForm(forms.ModelForm):
    Rating = forms.RadioSelect(choices=numbers)
    class Meta:
        model = Album
        fields = '__all__'
        widgets ={
            'release_date': forms.DateInput(attrs={'type':'date'}),
            'Rating' : forms.RadioSelect(choices=numbers),
        }