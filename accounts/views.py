from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required


@login_required
def protected_view(request):
    return render(request, 'accounts/protected.html')
