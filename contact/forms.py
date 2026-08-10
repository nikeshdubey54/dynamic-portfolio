from django import forms

from .models import ContactMessage


class ContactMessageForm(forms.ModelForm):

    class Meta:

        model = ContactMessage

        fields = [
            'name',
            'email',
            'subject',
            'message',
        ]

        widgets = {

            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your name',
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your email',
                }
            ),

            'subject': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter subject',
                }
            ),

            'message': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your message',
                    'rows': 6,
                }
            ),
        }

    def clean_name(self):

        name = self.cleaned_data.get('name')

        if name and len(name.strip()) < 2:

            raise forms.ValidationError(
                'Name must contain at least 2 characters.'
            )

        return name.strip()

    def clean_subject(self):

        subject = self.cleaned_data.get('subject')

        if subject and len(subject.strip()) < 3:

            raise forms.ValidationError(
                'Subject must contain at least 3 characters.'
            )

        return subject.strip()

    def clean_message(self):

        message = self.cleaned_data.get('message')

        if message and len(message.strip()) < 10:

            raise forms.ValidationError(
                'Message must contain at least 10 characters.'
            )

        return message.strip()