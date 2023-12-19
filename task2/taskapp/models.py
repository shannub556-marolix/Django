from django.db import models
import datetime
# Create your models here.
class Register(models.Model):
    Name=models.CharField(max_length=200)
    Email=models.CharField(max_length=200)
    Mobile=models.CharField(max_length=200)
    date_and_time=models.CharField(max_length=1000)



