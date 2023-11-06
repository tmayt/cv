from django.shortcuts import render
from random import choice, randint

def home(request):
    return render(request,'home.html')
