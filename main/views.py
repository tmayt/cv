from django.shortcuts import render
from main.models import Education,Qualification,Profile

def home(request):
    e = Education.objects.all()
    q = Qualification.objects.all()
    p = Profile.objects.first()
    context = {
        'educations': e,
        'qualifications': q,
        'profile': p
    }
    return render(request,'home.html',context)

