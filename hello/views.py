from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse  #import http resp fn from http module


def myView(request):
    return HttpResponse('hello world!')