from django.urls import path

from home.views import *

urlpatterns = [
    path('', home, name="home"),
    path('introduce/', introduce, name="introduce"),
    path('introduce/establish/', establish, name="establish"),
    path('introduce/directions/', directions, name="directions"),
    path('introduce/group/', group, name="group"),
    path('introduce/establishobject/', establishobject, name="establishobject"),
]