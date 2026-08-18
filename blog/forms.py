from django import forms

from .models import BlogPost


class BlogPostForm(forms.ModelForm):

    class Meta:

        model = BlogPost

        fields = [
            'title',
            'slug',
            'short_description',
            'content',
            'image',
            'author',
            'category',
            'featured',
            'is_active',
        ]

        widgets = {

            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter blog post title',
                }
            ),

            'slug': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'blog-post-slug',
                }
            ),

            'short_description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4,
                    'placeholder': 'Enter short description',
                }
            ),

            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 12,
                    'placeholder': 'Write your blog content...',
                }
            ),

            'image': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control',
                }
            ),

            'author': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Author name',
                }
            ),

            'category': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Python, Django, Web Development',
                }
            ),

            'featured': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                }
            ),

            'is_active': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                }
            ),
        }