from django.http import HttpResponse
from django.shortcuts import render
from .data import MENU_CATEGORIES

def home(request):
    return render(request, "index.html", {"categories": MENU_CATEGORIES})

def about(request):
    return render(request, "about.html")
