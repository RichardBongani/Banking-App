from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def home(request):
    return render(request, 'users/home.html')

def register(request):
    form = UserCreationForm()
    return render(request, 'users/register.html', {'form':form})
