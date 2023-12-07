from django.db import models
from categories.models import catagory
from Author.models import author

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    category = models.ManyToManyField(catagory)
    author = models.ForeignKey(author,on_delete=models.CASCADE)

    def __str__(self):
        return self.title