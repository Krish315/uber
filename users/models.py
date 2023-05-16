from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=25,null=True,blank=True)
    last_name = models.TextField(null=True,blank=True)
    DOB = models.DateField(max_length=6,null=True,blank=True)
    mobile = models.IntegerField(max_length=10,null=True,blank=True)
    Gender_types = (
        (1, 'male'),
        (2, 'female'),
        (3, 'other'),
    )
    Gender = models.IntegerField(
        max_length=10,
        choices = Gender_types,
        default = 1
    )
class Order(models.Model):
    Order_name= models.CharField(max_length=20,null=True,blank=True)
    Order_price= models.IntegerField(max_length=20,null=True,blank=True)
    Order_discount=models.IntegerField(max_length=20,null=True,blank=True)
    Order_quantity=models.IntegerField(max_length=5,null=True,blank=True)
    Order_address=models.TextField(max_length=20,null=True,blank=True)
    Order_date=models.DateField(max_length=10,null=True,blank=True)