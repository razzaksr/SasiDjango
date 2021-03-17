from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def greet(request):
    return HttpResponse("<h1>Zealous Welcomes you to learn DJANGO</h1>")

def hello(request):
    return render(request,'hai.html')
