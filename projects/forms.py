from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project

        fields = [
            'title',
            'short_description',
            'image',
            'technologies',
            'github_link',
            'live_demo',
            'featured',
        ]

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter project title',
                }
            ),

            'short_description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4,
                    'placeholder': 'Enter short description',
                }
            ),

            'image': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control',
                }
            ),

            'technologies': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Python, Django, Bootstrap',
                }
            ),

            'github_link': forms.URLInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'https://github.com/...',
                }
            ),

            'live_demo': forms.URLInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'https://...',
                }
            ),

            'featured': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                }
            ),
        }