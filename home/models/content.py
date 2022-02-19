from distutils.command.upload import upload
from django.db import models

class Content(models.Model):
    title=models.CharField(max_length=200)
    text=models.TextField(max_length=20000)
    author=models.CharField(max_length=50)
    slug=models.CharField(max_length=150 ,default="")
    time=models.DateTimeField()
    image=models.ImageField(upload_to='blog/image')
  

