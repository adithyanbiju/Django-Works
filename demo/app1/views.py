from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# function based

def home(request):

    return HttpResponse("welcome to Django")

def index(request):

    return HttpResponse("index page")