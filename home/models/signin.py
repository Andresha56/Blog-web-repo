
from pyexpat import model
from django.db import models

class Signin(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField( max_length=100)
    