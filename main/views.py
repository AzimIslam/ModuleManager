from django.shortcuts import render

from main.models import Module

def main_view(request):
    return render(request, 'main/index.html')
