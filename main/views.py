from django.shortcuts import render
from main.models import Education,Qualification,Profile,Message

def home(request):
    if request.method == "POST":
        # ezafe kardane data haye form be Message
        pass
    else:
        e = Education.objects.all()
        q = Qualification.objects.all()
        p = Profile.objects.first()
        context = {
            'educations': e,
            'qualifications': q,
            'profile': p
        }
        return render(request,'home.html',context)

