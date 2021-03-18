from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def greet(request):
    return HttpResponse("<h1>Zealous Welcomes you to learn DJANGO</h1>")

def hello(request):
    return render(request,'hai.html',{'domain':'Flask'})

def typeForm(request):
    return render(request,'Forming.html')

def respForm(request):
    one=int(request.POST['alpha'])
    two = int(request.POST['beta'])
    res=one*two
    return render(request,'check.html',{'result':res})
