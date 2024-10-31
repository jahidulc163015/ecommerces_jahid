from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Products (models.Model) : 
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    image=models.ImageField(upload_to='Product/',blank=True, null=True)

    
# class Vegetables (models.Model) : 
#     name = models.CharField(max_length=100)
#     category = models.CharField(max_length=100)
#     price = models.FloatField()
#     description = models.TextField()
#     image=models.ImageField(upload_to='vegetables/',blank=True, null=True)





class Contact(models.Model):
     name = models.CharField(max_length=100)
     email = models.CharField(max_length=100)
     message= models.CharField(max_length=100)





class Billing(models.Model):
     firstname = models.CharField(max_length=10)
     lastname=models.CharField(max_length=10)
     company =models.CharField(max_length=10)
     address=models.CharField(max_length=10)
     town=models.CharField(max_length=10)
     country=models.CharField(max_length=10)
     postcode=models.IntegerField(max_length=10)
     mobile=models.IntegerField(max_length=10)
     email=models.EmailField()


