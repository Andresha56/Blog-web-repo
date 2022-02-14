from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    phone_number=models.CharField(max_length=10)
    message=models.TextField(max_length=500)
    time=models.DateTimeField(auto_now_add=True)