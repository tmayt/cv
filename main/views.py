from django.shortcuts import render
from random import choice, randint

def home(request):
    context = {}
    return render(request,'home.html',context)

