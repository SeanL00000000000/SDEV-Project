from django.urls import path, include
from sdev_proj.views import *
urlpatterns = [
    path('',index, name='index'),

]
