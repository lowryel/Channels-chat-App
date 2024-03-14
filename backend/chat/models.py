from django.db import models

# Create your models here.


class Room(models.Model):
    room_name = models.CharField(max_length=64)

    def __str__(self):
        return str(self.room_name)

class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    sender = models.CharField(max_length=64)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.room)
