from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def category(request):
    if request.method == 'POST':
        category_form = forms.categoryform(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('home')
    else:
         category_form = forms.categoryform()
    return render(request, 'category.html',{'category_form':category_form})