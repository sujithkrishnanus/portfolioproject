from django.shortcuts import render
from .models import *

# Create your views here.

def createPersonal(request):
    pdetails= personalDetails.objects.all()
    educations=education.objects.all()
    experiences=experience.objects.all()
    projects=project.objects.all()
    socialMedias=socialMedia.objects.all()
    skills=skill.objects.all()

    context={
        'pdetails': pdetails,
        'educations':educations,
        'experiences':experiences,
        'projects':projects,
        'socialMedias':socialMedias,
        'skills':skills
    }

    return render(request,'index.html',context)

