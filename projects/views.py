from django.shortcuts import render , get_object_or_404
from .models import Project

def projects(request):

    projects = Project.objects.all().order_by('-created_at')

    featured_projects = Project.objects.filter(
        featured=True
    ).order_by('-created_at')

    context = {

        'projects': projects,

        'featured_projects': featured_projects,

    }

    return render(
        request,
        'projects/projects.html',
        context
    )


def project_detail(request, id):

    project = get_object_or_404(Project, id=id)

    context = {

        'project': project,

    }

    return render(
        request,
        'projects/project_detail.html',
        context
    )

