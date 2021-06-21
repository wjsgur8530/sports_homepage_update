from django.urls import path

from laboratorynews.views import *

urlpatterns = [
    path('laboratorynews/researchfield', researchfield, name="researchfield"),
    path('laboratorynews/thesisdata', thesisdata, name="thesisdata"),
    path('laboratorynews/researchproject', researchproject, name="researchproject"),
    path('laboratorynews/presentation', presentation, name="presentation"),
]