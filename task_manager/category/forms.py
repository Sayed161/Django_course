from django import forms
from .models import categories

class categoryform(forms.ModelForm):
    class Meta:
        model = categories
        fields = '__all__'