from django.shortcuts import render
from main.models import Education,Qualification,Profile,Message,AcademicProjectCategory

def home(request):
    log = None
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        text = request.POST['text']
        Message.objects.create(
            name=name,
            email=email,
            text=text
        )
        log = "We received your message"

    e = Education.objects.all()
    q = Qualification.objects.all()
    p = Profile.objects.first()
    a = AcademicProjectCategory.objects.all()

    context = {
        'educations': e,
        'qualifications': q,
        'profile': p,
        'AcademicProjectCategories': a,
        'log':log
    }
    return render(request,'home.html',context)

