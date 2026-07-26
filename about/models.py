from django.db import models


class About(models.Model):

    full_name = models.CharField(max_length=100)

    designation = models.CharField(max_length=150)

    short_bio = models.TextField()

    about_me = models.TextField()

    profile_image = models.ImageField(
        upload_to='profile/',
        blank=True,
        null=True
    )

    resume = models.FileField(
        upload_to='resume/',
        blank=True,
        null=True
    )

    email = models.EmailField()

    phone = models.CharField(max_length=20)

    location = models.CharField(max_length=150)

    github = models.URLField(blank=True)

    linkedin = models.URLField(blank=True)

    instagram = models.URLField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

class Education(models.Model):

    degree = models.CharField(max_length=200)

    institute = models.CharField(max_length=200)

    start_year = models.PositiveIntegerField()

    end_year = models.PositiveIntegerField()

    description = models.TextField(blank=True)

    def __str__(self):
        return self.degree


class Experience(models.Model):

    company = models.CharField(max_length=200)

    designation = models.CharField(max_length=200)

    start_date = models.CharField(max_length=50)

    end_date = models.CharField(max_length=50)

    description = models.TextField(blank=True)

    def __str__(self):
        return self.company

class Certification(models.Model):

    title = models.CharField(max_length=200)

    organization = models.CharField(max_length=200)

    issue_date = models.DateField()

    certificate_url = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Achievement(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField()

    achievement_date = models.DateField()

    def __str__(self):
        return self.title