# Generated by Django 5.0 on 2024-03-12 00:59

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("chat", "0002_rename_room_message_room_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="message",
            old_name="room_name",
            new_name="room",
        ),
    ]
