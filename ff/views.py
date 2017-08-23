from django.shortcuts import render
from .models import Skill

# Create your views here.
def generateImage(request):
    if request.method == 'GET':
        skills = Skill.objects.all().order_by('name')
        return render(request, 'ff/generateImage.html', {'hura': 'nudaaaa', 'skills': skills})
    if request.method == 'POST':
        return render(request, 'ff/generateImage.html', {'data': request.POST, 'hura': 'hura'})
