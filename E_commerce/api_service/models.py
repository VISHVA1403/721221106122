from django.db import models

# Create your models here.
class Company(models.Model):
    companyName = models.CharField(max_length=100)
    ownerName = models.CharField(max_length = 50)
    rollNo = models.IntegerField()
    ownerEmail = models.EmailField(unique=True)
    clientId = models.CharField(max_length=20, unique=True)
    clientSecret = models.CharField(max_length=40)
    def __str__(self):
        return self.company_name
    

class Product(models.Model):
    productName = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    rating = models.DecimalField(max_digits = 2, decimal_places=1)
    discount = models.IntegerField(default=0)
    availability = models.CharField(max_length = 15,default = "out-of-stock")

    def __str__(self):
        return self.productName