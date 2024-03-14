from django.urls import path

from .views import *

urlpatterns = [
    path("", createRoom, name="room"),
    path("<str:room>/<str:username>/", messageView, name="message"),
]


