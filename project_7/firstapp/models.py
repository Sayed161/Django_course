from django.db import models

# Create your models here.
class studentData(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    fatherName = models.CharField(max_length=20)
    address = models.TextField()