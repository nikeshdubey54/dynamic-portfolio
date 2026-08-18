from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .forms import SkillForm
from .models import Skill

def skills(request):

    context = {

        'frontend_skills': Skill.objects.filter(category='Frontend'),

        'backend_skills': Skill.objects.filter(category='Backend'),

        'database_skills': Skill.objects.filter(category='Database'),

        'tools_skills': Skill.objects.filter(category='Tools'),

        'cloud_skills': Skill.objects.filter(category='Cloud'),

        'other_skills': Skill.objects.filter(category='Other'),

    }

    return render(request,'skills/skills.html',context)

@login_required
def skill_list(request):

    skills = Skill.objects.all().order_by('category', 'name')

    context = {
        'skills': skills,
        'page_title': 'Manage Skills',
    }

    return render(
        request,
        'dashboard/skills/skill_list.html',
        context
    )


@login_required
def skill_create(request):

    if request.method == 'POST':

        form = SkillForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect(
                'dashboard:skill_list'
            )

    else:

        form = SkillForm()

    context = {
        'form': form,
        'page_title': 'Add Skill',
        'submit_text': 'Create Skill',
    }

    return render(
        request,
        'dashboard/skills/skill_form.html',
        context
    )


@login_required
def skill_update(request, id):

    skill = get_object_or_404(
        Skill,
        id=id
    )

    if request.method == 'POST':

        form = SkillForm(
            request.POST,
            instance=skill
        )

        if form.is_valid():

            form.save()

            return redirect(
                'dashboard:skill_list'
            )

    else:

        form = SkillForm(
            instance=skill
        )

    context = {
        'form': form,
        'skill': skill,
        'page_title': 'Edit Skill',
        'submit_text': 'Update Skill',
    }

    return render(
        request,
        'dashboard/skills/skill_form.html',
        context
    )


@login_required
def skill_delete(request, id):

    skill = get_object_or_404(
        Skill,
        id=id
    )

    if request.method == 'POST':

        skill.delete()

        return redirect(
            'dashboard:skill_list'
        )

    context = {
        'skill': skill,
    }

    return render(
        request,
        'dashboard/skills/skill_confirm_delete.html',
        context
    )