from django.shortcuts import render

# Create your views here.
def generateImage(request):
    if request.method == 'GET':
        return render(request, 'ff/generateImage.html', {'hura': 'nudaaaa'})
    if request.method == 'POST':
        return render(request, 'ff/generateImage.html', {'data': request.POST, 'hura': 'hura'})
