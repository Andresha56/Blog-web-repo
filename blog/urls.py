
from unicodedata import name
from django.urls import path
from . import views
urlpatterns = [
    path('',views.blog),
    path('<str:slug>/',views.blogPost,name='blogpost'),
]
