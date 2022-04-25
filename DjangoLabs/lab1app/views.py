from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse('Hello world. Home page of week 1 app')
# Create your views here.
