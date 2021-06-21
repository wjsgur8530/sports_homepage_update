from django.shortcuts import render

# Create your views here.
def researchfield(request):
    return render(request, 'researchfield.html')

def thesisdata(request):
    return render(request, 'thesisdata.html')

def researchproject(request):
    return render(request, 'researchproject.html')

def presentation(request):
    return render(request, 'presentation.html')