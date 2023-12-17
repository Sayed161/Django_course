from django import forms
from .models import Musician
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

# Create your models here.
type = [('Guiter','guiter'), ('Piano', 'piano'),('Violin','violin'),('Drums','drums'),('Vocal','vocal')]
class MusicianForm(forms.ModelForm):
     Instrument_type = forms.ChoiceField(choices=type)
     class Meta:
          model = Musician
          fields = '__all__'

class RegisterForm(UserCreationForm):
     class Meta:
        model = User
        fields = ['username','first_name','last_name','email']


class UserDataChange(UserChangeForm):
     password1 = None
     password2 = None
     class Meta:
        model = User
        fields = ['username','first_name','last_name','email']