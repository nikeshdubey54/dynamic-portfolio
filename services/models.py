from django.db import models


class Service(models.Model):

    title = models.CharField(max_length=100)

    short_description = models.TextField()

    description = models.TextField(blank=True)

    icon = models.CharField(
        max_length=100,
        blank=True
    )

    image = models.ImageField(
        upload_to='services/',
        blank=True,
        null=True
    )

    featured = models.BooleanField(
        default=False
    )

    order = models.PositiveIntegerField(
        default=0
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

        ordering = ['order', '-created_at']

        verbose_name = 'Service'

        verbose_name_plural = 'Services'

    def __str__(self):

        return self.title