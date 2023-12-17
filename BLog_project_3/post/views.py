from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from django.utils.decorators import method_decorator

@login_required
def add_post(request):
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            post_form.instance.author = request.user
            post_form.save()
            return redirect('add_post')
    else:
         post_form = forms.PostForm()
    return render(request,'add_category.html',{'form':post_form})



#Add post using class based views
@method_decorator(login_required,name='dispatch')
class AddPost(CreateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('home')
    def form_valid(self, form) :
        form.instance.author = self.request.user
        return super().form_valid(form) 

@login_required
def edit_post(request,id):
    post = models.Post.objects.get(pk=id)
    post_form = forms.PostForm(instance=post)
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST,instance=post)
        if post_form.is_valid():
            post_form.instance.author = request.user
            post_form.save()
            return redirect('home')
    return render(request,'add_category.html',{'form':post_form})

@method_decorator(login_required,name='dispatch')
class upatePost(UpdateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = "add_post.html"
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')


@login_required
def delete_post(request,id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('home')

@method_decorator(login_required,name='dispatch')
class DeletePost(DeleteView):
    model = models.Post
    template_name = "delete.html"
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')

class DetailClassView(DetailView):
    model = models.Post
    pk_url_kwarg = 'id'
    template_name = "post_details.html"

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data = self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comments = comment_form.save(commit=False)
            new_comments.post = post
            new_comments.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        if self.request.method == 'POST':
            comment_form = forms.CommentForm(data = self.request.POST)
            if comment_form.is_valid():
                new_comments = comment_form.save(commit=False)
                new_comments.post = post
                new_comments.save()
        else:
            comment_form = forms.CommentForm()
        
        context['comments']=comments
        context['comment_form']=comment_form
        return context
    