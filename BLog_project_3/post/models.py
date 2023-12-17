from django.db import models
from categories.models import catagory
from django.contrib.auth.models import User
from django.db.models import Model

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = models.ImageField(upload_to='./media/image', blank=True,null=True)
    category = models.ManyToManyField(catagory)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=50)
    email= models.EmailField(max_length=254)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return f"comments by {self.name}"