from django.db import models


class Project(models.Model):

    title = models.CharField(
        max_length=200
    )

    short_description = models.TextField()

    image = models.ImageField(
        upload_to='projects/'
    )

    technologies = models.CharField(
        max_length=300,
        help_text="Example: Python, Django, Bootstrap"
    )

    github_link = models.URLField(
        blank=True
    )

    live_demo = models.URLField(
        blank=True
    )

    featured = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title