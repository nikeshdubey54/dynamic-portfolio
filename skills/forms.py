from django import forms

from .models import Skill


class SkillForm(forms.ModelForm):

    class Meta:

        model = Skill

        fields = [
            'name',
            'category',
            'proficiency',
            'icon',
        ]

        widgets = {

            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter skill name',
                }
            ),

            'category': forms.Select(
                attrs={
                    'class': 'form-select',
                }
            ),

            'proficiency': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '0 - 100',
                    'min': 0,
                    'max': 100,
                }
            ),

            'icon': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'fa-brands fa-python',
                }
            ),
        }

    def clean_proficiency(self):

        proficiency = self.cleaned_data['proficiency']

        if proficiency < 0 or proficiency > 100:
            raise forms.ValidationError(
                'Proficiency must be between 0 and 100.'
            )

        return proficiency