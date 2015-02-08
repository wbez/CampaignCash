from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Explorer says hey there world!")