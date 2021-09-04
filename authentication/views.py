from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from authentication.models import CustomUser

def login():
    return HttpResponse("Hello World")