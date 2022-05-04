
from django.utils.translation import get_language,activate
from django.utils import translation
from django.utils.translation import gettext
# Create your views here.
from django.shortcuts import render

def index(request):


    return render(request, 'index.html',)

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

    return render(request, 'wrecks.html',)

