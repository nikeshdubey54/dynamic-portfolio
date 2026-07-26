from django.contrib import admin
from .models import About, Education, Experience ,Certification , Achievement


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):

    list_display = (
        'full_name',
        'designation',
        'email',
        'phone',
        'location',
        'created_at',
    )

    search_fields = (
        'full_name',
        'designation',
        'email',
        'phone',
    )

    list_filter = (
        'created_at',
        'updated_at',
    )

    ordering = (
        '-created_at',
    )

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):

    list_display = (
        'degree',
        'institute',
        'start_year',
        'end_year',
    )


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):

    list_display = (
        'company',
        'designation',
        'start_date',
        'end_date',
    )

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'organization',
        'issue_date',
    )

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):

    list_display = (

        'title',

        'achievement_date',

    )