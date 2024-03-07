from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    text = "<h1>Hello World!</h1>"
    text += "<a href='about/'>about</a><br>"
    text += "<a href='contact/>contact</a>"
    return HttpResponse(text)


def about(request):
    text = "<h1>Hello World!</h1>"
    text += "<a href='/'>bosh sahifa</a><br>"
    text += "<a href='contact/>contact</a>"
    return HttpResponse(text)


def contact(request):
    text = "<h1>3 sahifa</h1>"
    text += "<a href='/'>bosh sahifa</a>"
    text += "<a href='about/'>about</a><br>"
    return HttpResponse(text)
