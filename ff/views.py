from django.shortcuts import render
import json

# Create your views here.
def generateImage(request):
    sadf = request.POST['team1']
    return render(request, 'ff/generateImage.html', {'data': request.POST})
