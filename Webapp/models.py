from django.db import models

# Create your models here.
class register(models.Model):
    username = models.CharField(max_length=40 , null=True, blank=True)
    email = models.EmailField(max_length=20 , null=True, blank=True)
    password = models.CharField(max_length=8 , null=True, blank=True)


def __str__(self):
    return str(self.id)


class Products(models.Model):
    Productname = models.CharField(max_length=200,default="some_value")
    Productprize = models.FloatField(null=True, blank=True)
    Productquantity = models.CharField(max_length=20,default="some_value")
    Shopname = models.CharField(max_length=200,default="some_value")
    Productimage = models.CharField(max_length=200,default="some_value",null=True)


class AddtoCard(models.Model):
    productid = models.IntegerField(null=True, blank=True)