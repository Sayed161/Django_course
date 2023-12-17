from django.shortcuts import render,redirect
from .forms import RegisterForm,UserDataForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from car_model.models import Cars,Order

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

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            user_login_form = AuthenticationForm(request=request,data=request.POST)
            if user_login_form.is_valid():
                user_name = user_login_form.cleaned_data['username']
                user_pass = user_login_form.cleaned_data['password']
                user = authenticate(username=user_name, password=user_pass)
                if user is not None:
                    login(request,user)
                    return redirect('home')
        else:
            user_login_form = AuthenticationForm()
        return render(request,'register.html',{'form':user_login_form,'type':'Login'})
    else:
        return redirect('home')

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def profile_login(request):
    purchased = Order.objects.filter(user = request.user)
    return render(request,'profile.html',{'purchased':purchased})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        edit_form = UserDataForm(request.POST,instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            messages.success(request,"Profile Updated Successfully")
            return redirect('profile')
    else:
        edit_form = UserDataForm(instance=request.user)
    return render(request,'register.html',{'form':edit_form,'type':'Edit' })

