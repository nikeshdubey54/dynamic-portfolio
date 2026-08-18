from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    redirect,
    render,
    get_object_or_404,
)

from .forms import ContactMessageForm
from .models import ContactMessage


def contact(request):

    if request.method == 'POST':

        form = ContactMessageForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Your message has been sent successfully.'
            )

            return redirect('contact')

    else:

        form = ContactMessageForm()

    context = {
        'form': form,
    }

    return render(
        request,
        'contact/contact.html',
        context
    )


# ==========================================
# Dashboard Contact Message Management
# ==========================================

@login_required
def message_list(request):

    messages_list = ContactMessage.objects.all().order_by(
        '-created_at'
    )

    context = {
        'messages_list': messages_list,
        'page_title': 'Manage Messages',
    }

    return render(
        request,
        'dashboard/contact/message_list.html',
        context
    )


@login_required
def message_detail(request, id):

    message = get_object_or_404(
        ContactMessage,
        id=id
    )

    context = {
        'message': message,
    }

    return render(
        request,
        'dashboard/contact/message_detail.html',
        context
    )


@login_required
def message_toggle_read(request, id):

    message = get_object_or_404(
        ContactMessage,
        id=id
    )

    if request.method == 'POST':

        message.is_read = not message.is_read
        message.save(update_fields=['is_read'])

    return redirect(
        'dashboard:message_list'
    )


@login_required
def message_delete(request, id):

    message = get_object_or_404(
        ContactMessage,
        id=id
    )

    if request.method == 'POST':

        message.delete()

        return redirect(
            'dashboard:message_list'
        )

    context = {
        'message': message,
    }

    return render(
        request,
        'dashboard/contact/message_confirm_delete.html',
        context
    )

