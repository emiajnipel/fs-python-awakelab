from django.http import HttpResponse
from django.shortcuts import render

def portafolio(request):
    return render(request, 'index.html')