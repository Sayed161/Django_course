from django.db import models
from brand_model.models import brand
from django.contrib.auth.models import User
# Create your models here.
class Cars(models.Model):
    title = models.CharField(max_length=150)
    price = models.CharField(max_length=150)
    details = models.TextField()
    quantity = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='./media/image', blank=True,null=True)
    Brand = models.ForeignKey(brand,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    cars = models.ForeignKey(Cars, on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=50)
    email= models.EmailField(max_length=254)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return f"comments by {self.name}"
    

class Order(models.Model):
    products = models.ForeignKey(Cars, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    purchasedate = models.DateTimeField(auto_now_add=True)
    already_purchased = models.BooleanField(default=False)
    quantity_purchased = models.IntegerField(default=1)
    
    def __str__(self) -> str:
        return f"{self.products.title} - {self.user.username}"