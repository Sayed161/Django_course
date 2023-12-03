from django import forms
from django.core import validators

class contactForm(forms.Form):
    name = forms.CharField(label="User Name")
    email = forms.EmailField(label="Email")
    age = forms.IntegerField(label="Age")
    CHOICES = [('s',"small"), ("m","medium"), ('l','Large')]
    size = forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)
    meal = [('m','mashroom'), ("p","pepperoni"),('B','beef')]
    pizza = forms.MultipleChoiceField(choices=meal,widget=forms.CheckboxSelectMultiple)
    file = forms.FileField(label="File")
    Birthday = forms.DateField(widget = forms.DateInput(attrs={'type': 'date'}))
    Appoinment = forms.DateField(widget = forms.DateInput(attrs={'type': 'datetime-local'}))

# class StudentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.EmailField(widget=forms.EmailInput)
    # def clean_name(self):
    #     valName = self.cleaned_data['name']
    #     if len(valName)<10:
    #         raise forms.ValidationError("Please enter a name with at least 10charecter")
    #     return valName
    # def clean_email(self):
    #     valEmail = self.cleaned_data['email']
    #     if '.com' not in valEmail:
    #         raise forms.ValidationError("Please enter a valid email address with .com" )
    #     return valEmail
    # def clean(self):
    #     cleaned_data = super().clean()
    #     valName = self.cleaned_data['name']
    #     valEmail = self.cleaned_data['email']
    #     if '.com' not in valEmail:
    #         raise forms.ValidationError("Please enter a valid email address with .com" )
    #     elif len(valName)<10:
    #         raise forms.ValidationError("Please enter a name with at least 10charecter")
    #     else:
    #         return valName,valEmail

    
class StudentData(forms.Form):
    name = forms.CharField(widget=forms.TextInput,validators=[validators.MinLengthValidator(10,message="Please enter a name with at least 10charecter")])
    email = forms.EmailField(widget=forms.EmailInput,validators=[validators.EmailValidator])
    age = forms.IntegerField(validators=[validators.MaxValueValidator(35,message="Age must be At least 35"),validators.MinLengthValidator(18,message="Age must be at least 18")])
    file = forms.FileField(widget=forms.FileInput,validators=[validators.FileExtensionValidator('.png',message="Please enter a file with png format")])


class passwordValidation(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        valPass = self.cleaned_data["password"]
        valCOPass = self.cleaned_data["confirm_password"]
        valName = self.cleaned_data['name']
        if valPass != valCOPass :
            raise forms.ValidationError("password didn't match")
        if len(valName) < 10:
            raise forms.ValidationError("Name must be at least 10 characters")
         