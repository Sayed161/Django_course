from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def add_category(request):
    if request.method == 'POST':
        catagory_form = forms.CatagoryForm(request.POST)
        if catagory_form.is_valid():
            catagory_form.save()
            return redirect('add_category')
    else:
         catagory_form = forms.CatagoryForm()
    return render(request,'add_category.html',{'form':catagory_form})