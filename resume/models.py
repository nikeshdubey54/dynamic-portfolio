from django.db import models


class Resume(models.Model):

    name = models.CharField(
        max_length=100
    )

    designation = models.CharField(
        max_length=150
    )

    email = models.EmailField()

    phone = models.CharField(
        max_length=20,
        blank=True
    )

    location = models.CharField(
        max_length=150,
        blank=True
    )

    summary = models.TextField()

    resume_file = models.FileField(
        upload_to='resume/',
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        ordering = ['-created_at']

        verbose_name = 'Resume'

        verbose_name_plural = 'Resumes'

    def __str__(self):

        return self.name