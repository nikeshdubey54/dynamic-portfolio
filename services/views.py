from django.shortcuts import render

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