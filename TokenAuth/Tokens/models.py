from django.db import models


class User_Details(models.Model):
    username=models.CharField(primary_key=True,max_length=200)
    password=models.CharField(max_length=100)