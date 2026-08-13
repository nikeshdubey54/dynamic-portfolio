from django.shortcuts import render
from django.http import FileResponse, Http404

from .models import Resume


def resume_view(request):

    resume = Resume.objects.filter(
        is_active=True
    ).first()

    context = {
        'resume': resume,
    }

    return render(
        request,
        'resume/resume.html',
        context
    )


def resume_view_pdf(request):

    resume = Resume.objects.filter(
        is_active=True
    ).first()

    if not resume or not resume.resume_file:
        raise Http404("Resume is not available.")

    return FileResponse(
        resume.resume_file.open('rb'),
        content_type='application/pdf'
    )


def resume_download(request):

    resume = Resume.objects.filter(
        is_active=True
    ).first()

    if not resume or not resume.resume_file:
        raise Http404("Resume is not available.")

    return FileResponse(
        resume.resume_file.open('rb'),
        as_attachment=True,
        filename='Nikesh-Dubey-Resume.pdf',
        content_type='application/pdf'
    )