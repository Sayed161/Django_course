from typing import Any
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,update_session_auth_hash,logout
from django.contrib.auth.decorators import login_required
from post.models import Post
from . import forms
from django.contrib import messages
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
# Create your views here.


def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, "Registration Successfull")
            return redirect('user_login')
    else:
         register_form = forms.RegistrationForm()
    return render(request,'register.html',{'form':register_form,'type': 'Register'})


def user_login(request):
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
def profile(request):
    data = Post.objects.filter(author=request.user)   
    return render(request,'profile.html',{'data': data})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = forms.ChangeUserForm(request.POST,instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, "Profile Updated Successfull")
            return redirect('profile')
    else:
         profile_form = forms.ChangeUserForm(instance=request.user)
    return render(request,'update_profile.html',{'form':profile_form})


def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,data = request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Password updated Successfully")
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    else:
         form = PasswordChangeForm(user=request.user)
    return render(request,'change_pass.html',{'form':form})


def user_logout(request):
    logout(request)
    return redirect('user_login')


class LoginForm(LoginView):
    template_name = 'register.html'

    def get_success_url(self) -> str:
        return reverse_lazy('profile')
    

    def form_valid(self, form):
        messages.success(self.request, "Logged in successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, "Logged information incorrect")
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type']= 'login'
        return context
    
class LogOutForm(LogoutView):

    def get_success_url(self) -> str:
        return reverse_lazy('user_login')