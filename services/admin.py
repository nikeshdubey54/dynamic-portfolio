from django.contrib import admin

from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'featured',
        'is_active',
        'order',
        'created_at',
    )

    list_filter = (
        'featured',
        'is_active',
    )

    search_fields = (
        'title',
        'short_description',
        'description',
    )

    list_editable = (
        'featured',
        'is_active',
        'order',
    )

    ordering = (
        'order',
        '-created_at',
    )