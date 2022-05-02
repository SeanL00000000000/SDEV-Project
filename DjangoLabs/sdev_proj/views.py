from urllib import request

from django.shortcuts import render
from django.utils.translation import get_language,activate
from django.utils import translation
from django.utils.translation import gettext


def index(request):
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


