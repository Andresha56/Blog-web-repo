from django.contrib import admin

# Register your models here.

from blog.models import Blog

class AdminBlog(admin.ModelAdmin):
    list_display=['id','title','image']

admin.site.register(Blog,AdminBlog)