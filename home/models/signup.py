import statistics
from django.db import models

class Signup(models.Model):
    username=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField( max_length=100)
    re_password=models.CharField(max_length=100)
    

    @staticmethod
    def getuser_by_email(username):
        return Signup.objects.get(username=username)

    @staticmethod
    def getuser_by_password(re_password):
        return Signup.objects.get(password=re_password)