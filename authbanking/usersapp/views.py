from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse ('<h2>Welcome to King Bank</h2>')