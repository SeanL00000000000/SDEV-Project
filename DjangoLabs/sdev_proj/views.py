
from django.shortcuts import render

<<<<<<< HEAD
# Create your views here.
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')
=======

def index(request):
    return render(request, 'index.html',)
>>>>>>> ca9eca35c0c4a1315f7cad14bb9e7b664cf06cda
