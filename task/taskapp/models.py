from django.db import models

# Create your models here.
class Employee(models.Model):
    Fname=models.CharField(max_length=200)
    Lname=models.CharField(max_length=200)
    Email=models.CharField(max_length=200)
    Dob=models.CharField(max_length=200)
    Gender=models.CharField(max_length=200)
    Mobile=models.CharField(max_length=200)
    Domain=models.CharField(max_length=200)
    Company=models.CharField(max_length=200)
    Salary=models.CharField(max_length=200)

