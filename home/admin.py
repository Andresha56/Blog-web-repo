
from csv import list_dialects
from django.contrib import admin

# Register your models here.


from . models import Contact
from .models import Content

class Admincontact(admin.ModelAdmin):
    list_display=['id','name','email','time']

class Admincontent(admin.ModelAdmin):
    list_display=['id','author','image']

admin.site.register(Contact,Admincontact)
admin.site.register(Content,Admincontent)