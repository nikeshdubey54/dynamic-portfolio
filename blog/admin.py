from django.contrib import admin
from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'category',
        'author',
        'featured',
        'is_active',
        'created_at',
    )

    list_filter = (
        'category',
        'featured',
        'is_active',
        'created_at',
    )

    search_fields = (
        'title',
        'short_description',
        'content',
        'category',
    )

    prepopulated_fields = {
        'slug': ('title',)
    }

    list_editable = (
        'featured',
        'is_active',
    )

    ordering = (
        '-created_at',
    )