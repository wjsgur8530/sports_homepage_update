from django.urls import path
from member.views import *
urlpatterns = [
    path('member/login/', login, name="login"),
    path('member/logout/', logout, name="logout"),
]