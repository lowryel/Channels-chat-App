from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def createRoom(request):
    if request.method=="POST":
        username:str = request.POST["username"]
        room:str = request.POST["room"]
        try:
            get_room = Room.objects.get(room_name=room)
        except Room.DoesNotExist:
            new_room = Room(room_name=room)
            new_room.save()
        return redirect("message", username=username, room=room)
    return render(request, "home.html")


def messageView(request, room, username):
    get_room = Room.objects.get(room_name=room)
    # if get_room.DoesNotExist:
    #     return redirect("room")
    messages = Message.objects.filter(room=get_room)
    context = {
        "messages":messages,
        "username":username,
        "room":room
    }
    return render(request, "message.html", context)
