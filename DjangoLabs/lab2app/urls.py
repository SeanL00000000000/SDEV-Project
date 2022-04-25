from django.urls import path
from lab2app.views import *
urlpatterns = [
    path('',index, name='index'),
]
