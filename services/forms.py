from django import forms

from .models import Service


class ServiceForm(forms.ModelForm):

    class Meta:

        model = Service

        fields = [
            'title',
            'short_description',
            'description',
            'icon',
            'image',
            'featured',
            'order',
            'is_active',
        ]

        widgets = {

            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter service title',
                }
            ),

            'short_description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3,
                    'placeholder': 'Enter short description',
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 6,
                    'placeholder': 'Enter detailed service description',
                }
            ),

            'icon': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'bi bi-code-slash',
                }
            ),

            'image': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control',
                }
            ),

            'featured': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                }
            ),

            'order': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'min': 0,
                    'placeholder': 'Display order',
                }
            ),

            'is_active': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                }
            ),
        }