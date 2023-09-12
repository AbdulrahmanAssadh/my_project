
from django.urls import path
from  hotel.views import *

urlpatterns=[
    
     path('',index,name='hotel'),
     path('search',search,name='search')
]