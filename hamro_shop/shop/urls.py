from django.urls import path
from .views import *


urlpatterns = [
    
    path('', index, name="index"),
    path('category_filter/', category_filter, name="category_filter"),

    
]