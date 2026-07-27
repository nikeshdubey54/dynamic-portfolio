from django.db import models

# Create your models here.

class Skill(models.Model):

    CATEGORY_CHOICES = [
        ('Frontend', 'Frontend'),
        ('Backend', 'Backend'),
        ('Database', 'Database'),
        ('Tools', 'Tools'),
        ('Cloud', 'Cloud'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=100)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='Other'
    )

    proficiency = models.PositiveIntegerField(
        help_text="Enter value between 0 and 100"
    )

    icon = models.CharField(
        max_length=100,
        blank=True,
        help_text="Example: fa-python"
    )

    def __str__(self):
        return self.name
