from django.shortcuts import render

# Create your views here.
def generateImage(request):
    return render(request, 'ff/generateImage.html', {'hura': request.GET})
