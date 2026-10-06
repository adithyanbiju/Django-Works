from django.db import models
from django.forms import CharField


# Create your models here.
class Employee(models.Model):
    empid=models.IntegerField(unique=True)
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    place=models.CharField(max_length=30)

    gender_choices=[

        ('male','Male'),('female','Female'),

    ]
    gender=models.CharField(max_length=20,choices=gender_choices)


    joining_date=models.DateField()
    # joining_date = models.DateField(auto_now_add=True)
    salary=models.IntegerField()
    designation=models.CharField(max_length=30)




