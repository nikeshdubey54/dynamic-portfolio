from django.shortcuts import render
from .models import About, Education, Experience , Certification , Achievement


def about(request):

    context = {

        'about': About.objects.first(),

        'educations': Education.objects.all(),

        'experiences': Experience.objects.all(),

        'certifications': Certification.objects.all(),

        'achievements': Achievement.objects.all(),

    }

    return render(request, 'about/about.html', context)