from django.shortcuts import render
from .models import Skill

# Create your views here.
def skill_list(request):
    skills = Skill.objects.all().order_by('name')
    return render(request, 'skilllist/skill_list.html', {'skills': skills})