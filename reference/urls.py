from django.urls import path

from reference.views import *

urlpatterns = [
    path('reference/material/', material, name="material"),
    path('reference/material/create/', materialCreate, name="material_create"),
    path('reference/material/detail/<int:pk>/', materialDetail, name="material_detail"),
    path('reference/material/delete/<int:pk>/', materialDelete, name="material_delete"),
    path('reference/material/edit/<int:pk>/', materialEdit, name="material_edit"),
    path('reference/material/search/', materialsearchResult, name="material_search"),
    path('reference/photo/', photo, name="photo"),
    path('reference/photo/create/', photoCreate, name="photo_create"),
    path('reference/photo/detail/<int:pk>/', photoDetail, name="photo_detail"),
    path('reference/photo/delete/<int:pk>/', photoDelete, name="photo_delete"),
    path('reference/photo/edit/<int:pk>/', photoEdit, name="photo_edit"),
    path('reference/photo/search/', photolsearchResult, name="photo_search"),
]
