from django.db import models

class Signup(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField( max_length=200)
    re_password=models.CharField(max_length=200)
    