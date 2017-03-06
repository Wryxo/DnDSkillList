from django.shortcuts import render
from .models import Skill

# Create your views here.
def skill_list(request):
    skills = Skill.objects.all().order_by('name')
    return render(request, 'skilllist/skill_list.html', {'skills': skills})

def asheron(request):
    skills = Skill.objects.filter(pk__in=[19, 44, 40, 48, 39, 41, 61, 59, 29, 17]).order_by('name')
    return render(request, 'skilllist/skill_list.html', {'skills': skills})

def marjory(request):
    skills = Skill.objects.filter(pk__in=[60, 26, 21, 15, 13, 12, 11, 5, 1]).order_by('name')
    return render(request, 'skilllist/skill_list.html', {'skills': skills})