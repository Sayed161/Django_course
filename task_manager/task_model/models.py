from django.db import models
from category.models import categories
# Create your models here.
class task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    Assign_date = models.DateField()
    category = models.ManyToManyField(categories)

    def __str__(self) -> str:
        return self.title