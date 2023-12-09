from django import forms
from .models import albumsform

class AlbumForm(forms.ModelForm):
    class Meta:
        model = albumsform
        fields = '__all__'
        widgets ={
            'Album_release_date': forms.DateInput(attrs={'type':'date'})
        }