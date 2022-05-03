from urllib import request

from django.shortcuts import render
from django.utils.translation import get_language,activate
from django.utils import translation
from django.utils.translation import gettext

<<<<<<< HEAD
# Create your views here.
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')
=======

def index(request):
<<<<<<< HEAD
    return render(request, 'index.html',)
>>>>>>> ca9eca35c0c4a1315f7cad14bb9e7b664cf06cda
=======
    trans=translate(language='de')
    return render(request, 'index.html' ,{'trans':trans},)

def wrecks(request):
    return render(request, 'wrecks.html',)


def translate(language):
    cur_language=get_language()
    try:
        activate(language)
        text=gettext('hello')
    finally:
        activate(cur_language)
        return text


>>>>>>> 6bad32393a0131e202f4fadd277167d8f62058b9
