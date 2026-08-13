from django.db import models


class BlogPost(models.Model):

    title = models.CharField(max_length=200)

    slug = models.SlugField(
        unique=True
    )

    short_description = models.TextField()

    content = models.TextField()

    image = models.ImageField(
        upload_to='blog/',
        blank=True,
        null=True
    )

    author = models.CharField(
        max_length=100,
        default='Nikesh Dubey'
    )

    category = models.CharField(
        max_length=100,
        blank=True
    )

    featured = models.BooleanField(
        default=False
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

        verbose_name = 'Blog Post'

        verbose_name_plural = 'Blog Posts'

    def __str__(self):

        return self.title