from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from projects.models import Project
from skills.models import Skill
from blog.models import BlogPost
from contact.models import ContactMessage


@login_required
def dashboard_home(request):

    project_count = Project.objects.count()

    skill_count = Skill.objects.count()

    blog_count = BlogPost.objects.filter(
        is_active=True
    ).count()

    message_count = ContactMessage.objects.count()

    context = {
        "project_count": project_count,
        "skill_count": skill_count,
        "blog_count": blog_count,
        "message_count": message_count,
    }

    return render(
        request,
        "dashboard/dashboard.html",
        context
    )