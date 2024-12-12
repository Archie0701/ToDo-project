from django.http import HttpResponse
from django.shortcuts import render

def first_page(request):
    a = '<h1>Hello my dear</h1>'
    return render(request,'./index.html')