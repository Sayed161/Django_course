from .models import Cars,Comment
from django import forms

class CarsForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = '__all__'

class commentform(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email','body']