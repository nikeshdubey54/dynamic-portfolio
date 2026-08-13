from django.contrib import admin
from .models import Resume


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'designation',
        'email',
        'location',
        'is_active',
        'created_at',
    )

    list_filter = (
        'is_active',
        'created_at',
    )

    search_fields = (
        'name',
        'designation',
        'email',
        'location',
        'summary',
    )

    list_editable = (
        'is_active',
    )

    ordering = (
        '-created_at',
    )