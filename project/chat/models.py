import datetime

from django.db import models
from django.utils import timezone


class Room(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.CharField(max_length=40)
    room_name = models.CharField(max_length=140)
    created_on = models.DateTimeField(auto_now_add=True)
