from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def string1(request):
    return HttpResponse('<h1>This is my string1 application"</h1>')

def string2(request):
    return HttpResponse('<h1>This is my string2 application"</h1>')