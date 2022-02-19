from django.db import models

class Blog(models.Model):
    title=models.CharField(max_length=200)
    text=models.TextField(max_length=20000)
    author=models.CharField(max_length=50)
    time=models.DateTimeField()
    slug=models.CharField(max_length=150 ,default="")
    image=models.ImageField(upload_to='blog/image')