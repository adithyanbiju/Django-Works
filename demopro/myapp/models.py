from django.db import models

# Create your models here.

class Student(models.Model):
    roll_no=models.IntegerField()
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    place=models.CharField(max_length=30)
    marks=models.IntegerField()