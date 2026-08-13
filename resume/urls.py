from django.urls import path

from . import views


urlpatterns = [

    path(
        '',
        views.resume_view,
        name='resume'
    ),

    path(
        'view/',
        views.resume_view_pdf,
        name='resume_view_pdf'
    ),

    path(
        'download/',
        views.resume_download,
        name='resume_download'
    ),

]