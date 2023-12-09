from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.
def muscian_view(request):
    if request.method == 'POST':
        post_form = forms.MusicianForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('muscian')
    else:
         post_form = forms.MusicianForm()
    return render(request, 'muscian.html',{'form':post_form})