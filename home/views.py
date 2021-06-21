from django.shortcuts import render

# Create your views here.
from board.models import Board


def home(request):
    board = Board.objects.all().order_by('-pk')[:5]
    return render(request, 'home.html', {'board': board})

def introduce(request):
    return render(request, 'introduce.html')

def establish(request):
    return render(request, 'establish.html')

def directions(request):
    return render(request, 'directions.html')

def group(request):
    return render(request, 'group.html')

def establishobject(request):
    return render(request, 'establishobject.html')