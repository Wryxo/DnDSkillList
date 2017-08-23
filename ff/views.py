from django.shortcuts import render
import json

# Create your views here.
def generateImage(request):
    return render(request, 'ff/generateImage.html', {'data': request})
