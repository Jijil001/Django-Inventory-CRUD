from django.db import models
from django.core.validators import MinValueValidator

#All of our products
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6, validators=[MinValueValidator(0)])
    image = models.ImageField(upload_to='product_images/', null=True, blank=True) 
    stock = models.IntegerField()
    
    def __str__(self):
        return self.name