from django.shortcuts import render
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