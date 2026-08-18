from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ServiceForm
from .models import Service

def services(request):

    services_list = Service.objects.filter(
        is_active=True
    ).order_by(
        'order',
        '-created_at'
    )

    context = {
        'services': services_list,
    }

    return render(
        request,
        'services/services.html',
        context
    )

@login_required
def service_list(request):

    services = Service.objects.all().order_by(
        'order',
        '-created_at'
    )

    context = {
        'services': services,
        'page_title': 'Manage Services',
    }

    return render(
        request,
        'dashboard/services/service_list.html',
        context
    )


@login_required
def service_create(request):

    if request.method == 'POST':

        form = ServiceForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            return redirect(
                'dashboard:service_list'
            )

    else:

        form = ServiceForm()

    context = {
        'form': form,
        'page_title': 'Add Service',
        'submit_text': 'Create Service',
    }

    return render(
        request,
        'dashboard/services/service_form.html',
        context
    )


@login_required
def service_update(request, id):

    service = get_object_or_404(
        Service,
        id=id
    )

    if request.method == 'POST':

        form = ServiceForm(
            request.POST,
            request.FILES,
            instance=service
        )

        if form.is_valid():

            form.save()

            return redirect(
                'dashboard:service_list'
            )

    else:

        form = ServiceForm(
            instance=service
        )

    context = {
        'form': form,
        'service': service,
        'page_title': 'Edit Service',
        'submit_text': 'Update Service',
    }

    return render(
        request,
        'dashboard/services/service_form.html',
        context
    )


@login_required
def service_delete(request, id):

    service = get_object_or_404(
        Service,
        id=id
    )

    if request.method == 'POST':

        service.delete()

        return redirect(
            'dashboard:service_list'
        )

    context = {
        'service': service,
    }

    return render(
        request,
        'dashboard/services/service_confirm_delete.html',
        context
    )