import datetime

from django.db import models
from django.utils import timezone

class RoomIndex(models.Model):
    room_name = models.CharField(max_length=140)
    created_on = models.DateTimeField('date created')

    def was_created_on(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.created_on <= now
