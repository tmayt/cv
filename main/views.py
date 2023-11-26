from django.shortcuts import render
from main.models import Education,Qualification

def home(request):
    e = Education.objects.all()
    q = Qualification.objects.all()
    context = {
        'educations': e,
        'qualifications':q
    }
    return render(request,'home.html',context)

