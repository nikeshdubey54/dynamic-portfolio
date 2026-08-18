from django.urls import path

from . import views
from projects import views as project_views
from skills import views as skill_views
from blog import views as blog_views
from contact import views as contact_views
from services import views as service_views

app_name = 'dashboard'


urlpatterns = [

    # Dashboard Home

    path(
        '',
        views.dashboard_home,
        name='home'
    ),


    # =========================
    # Project Management
    # =========================

    path(
        'projects/',
        project_views.project_list,
        name='project_list'
    ),

    path(
        'projects/create/',
        project_views.project_create,
        name='project_create'
    ),

    path(
        'projects/<int:id>/edit/',
        project_views.project_update,
        name='project_update'
    ),

    path(
        'projects/<int:id>/delete/',
        project_views.project_delete,
        name='project_delete'
    ),

    # =========================
    # Skill Management
    # =========================

    path(
        'skills/',
        skill_views.skill_list,
        name='skill_list'
    ),

    path(
        'skills/create/',
        skill_views.skill_create,
        name='skill_create'
    ),

    path(
        'skills/<int:id>/edit/',
        skill_views.skill_update,
        name='skill_update'
    ),

    path(
        'skills/<int:id>/delete/',
        skill_views.skill_delete,
        name='skill_delete'
    ),

    # =========================
    # Blog Management
    # =========================

    path(
        'blog/',
        blog_views.blog_manage_list,
        name='blog_list'
    ),

    path(
        'blog/create/',
        blog_views.blog_create,
        name='blog_create'
    ),

    path(
        'blog/<int:id>/edit/',
        blog_views.blog_update,
        name='blog_update'
    ),

    path(
        'blog/<int:id>/delete/',
        blog_views.blog_delete,
        name='blog_delete'
    ),



    # =========================
    # Contact Message Management
    # =========================

    path(
        'messages/',
        contact_views.message_list,
        name='message_list'
    ),

    path(
        'messages/<int:id>/',
        contact_views.message_detail,
        name='message_detail'
    ),

    path(
        'messages/<int:id>/toggle-read/',
        contact_views.message_toggle_read,
        name='message_toggle_read'
    ),

    path(
        'messages/<int:id>/delete/',
        contact_views.message_delete,
        name='message_delete'
    ),


    # =========================
    # Service Management
    # =========================

    path(
        'services/',
        service_views.service_list,
        name='service_list'
    ),

    path(
        'services/create/',
        service_views.service_create,
        name='service_create'
    ),

    path(
        'services/<int:id>/edit/',
        service_views.service_update,
        name='service_update'
    ),

    path(
        'services/<int:id>/delete/',
        service_views.service_delete,
        name='service_delete'
    ),



]