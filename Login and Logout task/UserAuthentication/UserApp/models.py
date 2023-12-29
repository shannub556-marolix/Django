from django.db import models

# Create your models here.
class UserApp(models.Model):
    username=models.CharField(max_length=200,primary_key=True)
    password=models.CharField(max_length=200)