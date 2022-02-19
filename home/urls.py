
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='homePage'),
    path('about',views.about),
    path('contact',views.contact,name='contactpage'),
    path('search',views.search)
    
]
