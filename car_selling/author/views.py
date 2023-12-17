from django.shortcuts import render,redirect
from .forms import RegisterForm,UserDataForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from car_model.models import Cars,Order
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
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
        context['type']= 'Login'
        return context



class LogOutForm(LogoutView):

    def get_success_url(self) -> str:
        return reverse_lazy('login')


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

