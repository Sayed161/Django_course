from django.db import models
# Create your models here.
type= [('Guiter','guiter'),('Piano','piano'),('Violin','violin'),('Drum','drum')]
class Musician(models.Model):
    first_name  = models.CharField(max_length=30)
    last_name  = models.CharField(max_length=30)
    email  = models.EmailField()
    phone_number  = models.IntegerField()
    Instrument_type  = models.CharField(max_length=100)
    

    def __str__(self):
        return self.first_name