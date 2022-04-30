from django.urls import path
from sdev_proj.views import *
urlpatterns = [
    path('',index, name='index'),
]
