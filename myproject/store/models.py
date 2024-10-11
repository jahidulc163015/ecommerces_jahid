from django.db import models

# Create your models here.

class Products (models.Model) : 
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    image=models.ImageField(upload_to='Product/',blank=True, null=True)