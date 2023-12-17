from django.shortcuts import render,redirect
from django.views.generic import DetailView
from .models import Order,Cars
from . import forms
from django.contrib.auth.decorators import login_required

# Create your views here.
class Details(DetailView):
    model = Cars
    pk_url_kwarg = 'id'
    template_name = "details.html"

    def post(self, request, *args, **kwargs):
        comment_form = forms.commentform(data = self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.cars = post
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        comment_form = forms.commentform()
        
        context['comments']=comments
        context['comment_form']=comment_form
        return context
    

@login_required
def buy_car(request,pk):
    car = Cars.objects.get(pk = pk)
    purchase, created = Order.objects.get_or_create(user=request.user,products=car)

    if car.quantity > 0 and not purchase.already_purchased:
        purchase.already_purchased = True
        purchase.quantity_purchased+=1
        purchase.save()
        car.quantity-=1
        car.save()
        return redirect('profile')
    elif car.quantity > 0 and purchase.already_purchased:
        purchase.quantity_purchased+=1
        purchase.save()
        car.quantity-=1
        car.save()
        return redirect('profile')
    return render(request,'details.html',{'car':car,'purchase':purchase.already_purchased})