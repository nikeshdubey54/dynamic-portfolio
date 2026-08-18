from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from .models import Project
from .forms import ProjectForm

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

@login_required
def project_list(request):

    projects = Project.objects.all().order_by('-created_at')

    context = {
        'projects': projects,
        'page_title': 'Manage Projects',
    }

    return render(
        request,
        'dashboard/projects/project_list.html',
        context
    )


@login_required
def project_create(request):

    if request.method == 'POST':

        form = ProjectForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            return redirect(
                'dashboard:project_list'
            )

    else:

        form = ProjectForm()

    context = {
        'form': form,
        'page_title': 'Add Project',
        'submit_text': 'Create Project',
    }

    return render(
        request,
        'dashboard/projects/project_form.html',
        context
    )


@login_required
def project_update(request, id):

    project = get_object_or_404(
        Project,
        id=id
    )

    if request.method == 'POST':

        form = ProjectForm(
            request.POST,
            request.FILES,
            instance=project
        )

        if form.is_valid():

            form.save()

            return redirect(
                'dashboard:project_list'
            )

    else:

        form = ProjectForm(
            instance=project
        )

    context = {
        'form': form,
        'project': project,
        'page_title': 'Edit Project',
        'submit_text': 'Update Project',
    }

    return render(
        request,
        'dashboard/projects/project_form.html',
        context
    )


@login_required
def project_delete(request, id):

    project = get_object_or_404(
        Project,
        id=id
    )

    if request.method == 'POST':

        project.delete()

        return redirect(
            'dashboard:project_list'
        )

    context = {
        'project': project,
    }

    return render(
        request,
        'dashboard/projects/project_confirm_delete.html',
        context
    )

