from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
import random, time

# Create your views here.

def index(request):
    return render(request, 'home.html', {}, context_instance=RequestContext(request))

# These functions are referred in home.html and in DAWebServer/urls.py
def get_sense1(request):
    results =  round(random.random(), 3) # Your Python function for reading sensor 1 values
    print(results)
    return HttpResponse(results)

def get_sense2(request):
    results = round(random.random(), 3) # Your Python function for reading sensor 2 values
    print(results)
    return HttpResponse(results)