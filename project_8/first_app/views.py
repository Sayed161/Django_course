from django.shortcuts import render,redirect
from .forms import RegisterForm,UserChange
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash

# Create your views here.
def SignUp(request):
    if not request.user.is_authenticated:
        if request.method =='POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request,'Account has been registered')
                form.save()
        else:
            form = RegisterForm()
        return render(request, 'signup.html', {'form': form})
    else:
        return redirect('Profile')

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
                    return redirect('Profile')
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    else:
        return redirect('Profile')
   


def home(request):
    return render(request, 'home.html')


def profile(request):
    if request.user.is_authenticated:
        if request.method =='POST':
            form = UserChange(request.POST,instance=request.user)
            if form.is_valid():
                messages.success(request,'Account has been updated successfully')
                form.save()
        else:
            form = UserChange(instance=request.user)
        return render(request, 'profile.html', {'form': form})
    else:
        return redirect('SignUp')
    
def user_logout(request):
    logout(request)
    return redirect('Login')

def change_pass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user,data = request.POST )
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                return redirect('Profile')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request,'passchange.html',{'form': form})
    else:
        return redirect('Login')

def change_pass2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user,data = request.POST )
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                return redirect('Profile')
        else:
            form = SetPasswordForm(user=request.user)
        return render(request,'passchange.html',{'form': form})
    else:
        return redirect('Login')



def changeUser(request):
    if not request.user.is_authenticated:
        if request.method =='POST':
            form = UserChange(request.POST,instance=request.user)
            if form.is_valid():
                messages.success(request,'Account has been updated successfully')
                form.save()
        else:
            form = UserChange()
        return render(request, 'profile.html', {'form': form})
    else:
        return redirect('Profile')
