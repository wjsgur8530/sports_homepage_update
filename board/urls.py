from django.urls import path
from board.views import *
urlpatterns = [
    path('board/', board, name="board"),
    path('board/create/', boardCreate, name="create"),
    path('board/detail/<int:pk>/', boardDetail, name="detail"),
    path('board/search/', searchResult, name="search"),
]