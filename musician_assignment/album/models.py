from django.db import models
from musician.models import Musician

# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=70)
    release_date = models.DateField()
    Rating = models.IntegerField()
    musician = models.ForeignKey(Musician,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
