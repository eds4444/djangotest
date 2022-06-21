from django.urls import path

from .views import *

urlpatterns = [
    path( '', index ),  #http://127.0.0.1:8000/
    path( 'cats/<slug:cat>/', categories ),  #http://127.0.0.1:8000/cats/1/

]


