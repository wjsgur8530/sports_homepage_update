from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from board.forms import BoardForm
from board.models import Board


def board(request):
    board = Board.objects.all().order_by('-pk')
    page = request.GET.get('page', '1')
    paginator = Paginator(board, '10')
    page_obj = paginator.get_page(page)
    context = {
        'board': board,
        'page_obj': page_obj,
    }
    return render(request, 'board.html', context)

def boardCreate(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        user = request.user
        board = Board(
            title=title,
            content=content,
            user=user,
        )
        board.save()
        return redirect('board')
    else:
        boardForm = BoardForm
        context = {
            'boardForm': boardForm,
        }
        return render(request, 'board_create.html', context)

def boardDetail(request, pk):
    board_detail = get_object_or_404(Board, pk=pk)
    return render(request, 'board_detail.html', {'board_detail': board_detail})

def boardEdit(request, pk):
    board = Board.objects.get(id=pk)
    if request.method == "POST":
        board.title = request.POST['title']
        board.content = request.POST['content']
        board.user = request.user
        board.save()
        return redirect('board')
    else:
        boardForm = BoardForm
        return render(request, 'board_edit.html', {'boardForm':boardForm, 'board': board})

def boardDelete(request, pk):
    board = Board.objects.get(id=pk)
    board.delete()
    return redirect('board')

def searchResult(request):
    boards = None
    query = None
    if 'search' in request.GET:
        query = request.GET.get('search')
        boards = Board.objects.all().filter(Q(title=query) | Q(title__contains=query) | Q(content=query) | Q(content__contains=query)).order_by('-pk')
        page = request.GET.get('page', '1')
        paginator = Paginator(boards, '10')
        page_obj = paginator.page(page)
        return render(request, 'search.html', {'query': query, 'boards': boards, 'page_obj': page_obj})
    else:
        return render(request, 'search.html', {'query': query, 'boards': boards})
