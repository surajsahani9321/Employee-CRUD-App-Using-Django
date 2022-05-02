from distutils.command.upload import upload
from django.db import models
from django.forms import ImageField

# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=50)
    empid=models.IntegerField(max_length=20)
    branch=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    mobile=models.IntegerField(max_length=12)
    address=models.CharField(max_length=50)
    images=models.ImageField(upload_to='images')
    register_date=models.DateTimeField(auto_now_add=True)