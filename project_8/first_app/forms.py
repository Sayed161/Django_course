from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

class UserChange(UserCreationForm):
    password1 = None
    password2 = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']