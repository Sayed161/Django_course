from django.db import models
from django.utils.text import slugify
# Create your models here.
class brand(models.Model):
    name = models.CharField(max_length=100)
    brand_image = models.ImageField()
    slug = models.SlugField(max_length=100,null=True, blank=True,unique=True)

    def __str__(self) -> str:
        return self.name

