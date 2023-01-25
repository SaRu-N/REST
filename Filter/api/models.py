from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField(unique=True)
    city=models.CharField(max_length=100)
    enrolled_by =models.CharField(max_length=100)