from django.db import models

# Create your models here.
class UserRegister(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    password = models.CharField(max_length=12)

# def __str__(self):
#     return str(self.name)+" "+ str(self.number)
class Category(models.Model):
    CategoryName = models.CharField(max_length=20)
    image = models.ImageField(upload_to='CategoryImages', blank=True)
    def __str__(self):
        return self.CategoryName

class Product(models.Model):
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to="ProductImages", blank=True)
    price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField()

class Contactus(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    message=models.TextField()

class Order(models.Model):
    userid=models.CharField(max_length=200)
    productid=models.CharField(max_length=200)
    quantity=models.CharField(max_length=200)
    price=models.CharField(max_length=200)
    datetime=models.DateTimeField(auto_created=True,auto_now=True)
    paymentmethod=models.CharField(max_length=200)
    transactionid=models.CharField(max_length=200)

