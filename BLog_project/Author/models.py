from django.db import models

# Create your models here.
class author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    phone_number = models.CharField(max_length=30)

    def __str__(self):
        return self.name