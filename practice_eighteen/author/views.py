from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,SetPasswordForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            register_form = RegisterForm(request.POST)
            if register_form.is_valid():
                messages.success(request, "Registration Successfull" )
                register_form.save()
        else:
            register_form = RegisterForm()
        return render(request,'register.html',{'form': register_form, 'type': 'Register'} )
    else:
        return redirect('home')
    


def Login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username = user_name, password = user_pass)
            if user is not None:
                messages.success(request, "Logged in Successfull")
                login(request,user)
                return redirect('profile')
            else:
                messages.warning(request, "Login information is incorrect")
                return redirect('register')
    else:
        form = AuthenticationForm()
    return render(request,'register.html',{'type': 'Login','form':form})

@login_required
def LogOut(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect('login')

@login_required
def profile(request):  
    return render(request,'profile.html')


def edit_pass(request):
    if request.method == 'POST':
        form = SetPasswordForm(request.user,data= request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Password updated Successfully")
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    else:
        form = SetPasswordForm(user=request.user)
    return render(request,'edit.html',{'form':form})
