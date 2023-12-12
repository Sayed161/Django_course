from django.shortcuts import render
from post.models import Post
from categories.models import catagory
# Create your views here.
def home(request,catagory_slug=None):
    data = Post.objects.all()
    if catagory_slug is not None:
        category = catagory.objects.get(slug=catagory_slug)
        data = Post.objects.filter(category=category)
    Catagories = catagory.objects.all()
    print(data)
    return render(request, 'home.html',{'data':data, 'catagories':Catagories})