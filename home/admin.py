
from csv import list_dialects
from django.contrib import admin

# Register your models here.


from . models import Contact
from .models import Content
from .models import signup

class Admincontact(admin.ModelAdmin):
    list_display=['id','name','email','time']

class Admincontent(admin.ModelAdmin):
    list_display=['id','author','image']

class Adminsignup(admin.ModelAdmin):
    list_display=["id",'username',"email"]



admin.site.register(Contact,Admincontact)
admin.site.register(Content,Admincontent)
admin.site.register(signup.Signup,Adminsignup)