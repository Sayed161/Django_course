from django.shortcuts import render,redirect
from . import forms
from . import models

# Create your views here.
def album(request):
    if request.method == 'POST':
        post_form = forms.AlbumForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('album')
    else:
         post_form = forms.AlbumForm()
    return render(request, 'album.html',{'form':post_form})

def edit(request,id):
    if request.user.is_authenticated:
        post = models.Album.objects.get(pk=id)
        post_form = forms.AlbumForm(instance=post)
        if request.method == 'POST':
            post_form = forms.AlbumForm(request.POST, instance=post)
            if post_form.is_valid():
                post_form.save()
                return redirect('home')
        return render(request, 'album.html', {'form': post_form})
    else:
        return redirect('home')

def post_delete(request,id):
    if request.user.is_authenticated:
        post = models.Album.objects.get(pk=id)
        post.delete()
        return redirect('home')
    else:
        return redirect('home')
