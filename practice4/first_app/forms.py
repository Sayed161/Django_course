from django import forms
import datetime

Data= [('name','Name'),('email','Email'),('password','Password')]
birthyear=['1800','1900','2000']

class LoginForm(forms.Form):
    name = forms.CharField(max_length=30,initial='YOUR NAME')
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 1}))
    email = forms.EmailField()
    agree = forms.BooleanField()
    date = forms.DateField()
    data = forms.ChoiceField(choices=Data)
    today = forms.DateField(initial=datetime.date.today)
    choices = forms.ChoiceField(widget=forms.RadioSelect,choices=Data)
    password = forms.CharField(widget = forms.PasswordInput()) 
    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982', '1983', '1984']
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))