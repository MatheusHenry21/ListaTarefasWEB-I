from django.shortcuts import render
from django.http import HttpRequest

def home(request: HttpRequest):
    return render(request, 'index.html')

def add(request: HttpRequest):
    return render(request, 'adicionar.html')