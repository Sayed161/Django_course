from django.db import models
from Muscian.models import Musician
# Create your models here.
class albumsform(models.Model):
    Album_name = models.CharField(max_length=80)
    Album_release_date = models.DateField()
    Rating = models.CharField(max_length=20)
    musician = models.ForeignKey(Musician,on_delete=models.CASCADE,default=None)

    def __str__(self) -> str:
        return self.Album_name