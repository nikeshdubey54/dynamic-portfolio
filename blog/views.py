from django.shortcuts import render, get_object_or_404
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