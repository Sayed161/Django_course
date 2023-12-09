from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.
def albums(request):
    if request.method == 'POST':
        post_form = forms.AlbumForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            redirect('home')
    else:
        post_form = forms.AlbumForm()
    return render(request, 'albums.html', {'form': post_form})

def edit(request,id):
    post = models.albumsform.objects.get(pk=id)
    post_form = forms.AlbumForm(instance=post)
    if request.method == 'POST':
        post_form = forms.AlbumForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('home')
    return render(request, 'albums.html', {'form': post_form})

def delete(request,id):
    post = models.albumsform.objects.get(pk=id)
    post.delete()
    return redirect('home')
