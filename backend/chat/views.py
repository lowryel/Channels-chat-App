from django.shortcuts import render, redirect
from .models import *
import json
from datetime import datetime as Datetime
# Create your views here.
from django.core.cache import cache

def createRoom(request):
    if request.method=="POST":
        username:str = request.POST["username"]
        room:str = request.POST["room"]
        room_json=json.dumps({"data": ({"room":room, "created_at":Datetime.now().timestamp()})})
        cache.set("room", room_json, 60*60*24)
        if cache.get("room"):
            print(f'Room cached successfully: {cache.get("room")}')
        # cache.set("create_at", Datetime.now().timestamp())
        try:
            get_room = Room.objects.get(room_name=room)
        except Room.DoesNotExist:
            new_room = Room(room_name=room)
            new_room.save()
        return redirect("message", username=username, room=room)
    return render(request, "home.html")


def messageView(request, room, username):
    get_room = Room.objects.get(room_name=room)

    room_name = cache.get("room")
    get_room_name = json.loads(room_name)

    if get_room.room_name != get_room_name["data"]["room"]:
        return redirect("createRoom")

    messages = Message.objects.filter(room=get_room)
    context = {
        "messages":messages,
        "username":username,
        "room":room
    }
    return render(request, "message.html", context)
