from django import forms
from .models import brand

class BrandForm(forms.ModelForm):
    class Meta:
        model = brand
        fields = '__all__'