from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import BlogPostForm
from .models import BlogPost

def blog_list(request):

    featured_post = BlogPost.objects.filter(
        is_active=True,
        featured=True
    ).first()

    posts = BlogPost.objects.filter(
        is_active=True
    ).exclude(
        id=featured_post.id if featured_post else None
    )

    context = {
        'featured_post': featured_post,
        'posts': posts,
    }

    return render(
        request,
        'blog/blog.html',
        context
    )


def blog_detail(request, slug):

    post = get_object_or_404(
        BlogPost,
        slug=slug,
        is_active=True
    )

    context = {
        'post': post
    }

    return render(
        request,
        'blog/blog_detail.html',
        context
    )

@login_required
def blog_manage_list(request):

    posts = BlogPost.objects.all().order_by('-created_at')

    context = {
        'posts': posts,
        'page_title': 'Manage Blog Posts',
    }

    return render(
        request,
        'dashboard/blog/blog_list.html',
        context
    )


@login_required
def blog_create(request):

    if request.method == 'POST':

        form = BlogPostForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            return redirect(
                'dashboard:blog_list'
            )

    else:

        form = BlogPostForm()

    context = {
        'form': form,
        'page_title': 'Add Blog Post',
        'submit_text': 'Create Blog Post',
    }

    return render(
        request,
        'dashboard/blog/blog_form.html',
        context
    )


@login_required
def blog_update(request, id):

    post = get_object_or_404(
        BlogPost,
        id=id
    )

    if request.method == 'POST':

        form = BlogPostForm(
            request.POST,
            request.FILES,
            instance=post
        )

        if form.is_valid():

            form.save()

            return redirect(
                'dashboard:blog_list'
            )

    else:

        form = BlogPostForm(
            instance=post
        )

    context = {
        'form': form,
        'post': post,
        'page_title': 'Edit Blog Post',
        'submit_text': 'Update Blog Post',
    }

    return render(
        request,
        'dashboard/blog/blog_form.html',
        context
    )


@login_required
def blog_delete(request, id):

    post = get_object_or_404(
        BlogPost,
        id=id
    )

    if request.method == 'POST':

        post.delete()

        return redirect(
            'dashboard:blog_list'
        )

    context = {
        'post': post,
    }

    return render(
        request,
        'dashboard/blog/blog_confirm_delete.html',
        context
    )