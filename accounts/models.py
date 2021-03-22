from django.db import models


# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=25,null=True)
    phone=models.CharField(max_length=10,null=True)
    email=models.EmailField(max_length=25,null=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name
class Tag(models.Model):
    name=models.CharField(max_length=25,null=True)

    def __str__(self):
        return self.name
class Product(models.Model):
    CATEGORY=(('In door','In door'),('Out door','Out door'))
    name=models.CharField(max_length=25,null=True)
    price=models.FloatField(null=True)
    category=models.CharField(max_length=25,null=True,choices=CATEGORY)
    description=models.CharField(max_length=25,null=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    tag=models.ManyToManyField(Tag)
    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS=(
        ('Pending','Pending'),('Out for delivery','Out for delivery'),('Delivered','Delivered')
    )
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    status=models.CharField(max_length=250,choices=STATUS,null=True)
    customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    product=models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
