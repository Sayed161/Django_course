from django import forms
from .models import albumsform

class AlbumForm(forms.ModelForm):
    class Meta:
        model = albumsform
        fields = '__all__'