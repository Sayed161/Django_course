from django import forms
from .models import author

class AuthorForm(forms.ModelForm):
    class Meta:
        model = author
        fields = '__all__'