from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_polls(request):
    return HttpResponse('Hello Polls App')