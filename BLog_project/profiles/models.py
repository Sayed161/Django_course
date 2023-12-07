from django.db import models
from Author.models import author
# Create your models here.
class Profiles(models.Model):
    name = models.CharField(max_length=30)
    about = models.TextField()
    author = models.OneToOneField(author,on_delete=models.CASCADE,default=None) 

    def __str__(self):
        return self.name