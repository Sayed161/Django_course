from django.shortcuts import render,redirect
from . import forms
from .forms import RegisterForm,UserDataChange
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def musician(request):
    if request.method == 'POST':
        post_form = forms.MusicianForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('musician')
    else:
         post_form = forms.MusicianForm()
    return render(request,'musician.html',{'form':post_form})

def register(request):
    if not request.user.is_authenticated:
        if request.method =='POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request,'Account has been registered')
                form.save()
        else:
            form = RegisterForm()
        return render(request, 'register.html', {'form': form,'type':'Register'})
    else:
        return redirect('profile')
    
def Login(request):
    if  not request.user.is_authenticated:
        if request.method =='POST':
            form = AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username = name, password = userpass)#checking password if there is in it database
                if user is not None:
                    login(request,user)
                    return redirect('profile')
        else:
            form = AuthenticationForm()
        return render(request, 'register.html', {'form': form,'type':'Login'})
    else:
        return redirect('profile')
    


def user_logout(request):
    logout(request)
    return redirect('login')

def profile(request):
    if request.user.is_authenticated:
        if request.method =='POST':
            form = UserDataChange(request.POST,instance=request.user)
            if form.is_valid():
                messages.success(request,'Account has been updated successfully')
                form.save()
        else:
            form = UserDataChange(instance=request.user)
        return render(request, 'profile.html', {'form': form})
    else:
        return redirect('register')