from django import forms
from firstapp import models

class studentforms(forms.ModelForm):
    class Meta :
        model = models.studentData
        fields = '__all__'
        labels = {
            'name ': 'Student name',
            'roll' : 'Student roll',
            'address' : 'Student address'
        }