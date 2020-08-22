from django.db import models
from core import models as Core_models


class List(Core_models.TimeStampedModel):

    """ List Model Defination """

    name = models.CharField(max_length=80)
    user = models.ForeignKey("users.user", on_delete=models.CASCADE)
    rooms = models.ManyToManyField("rooms.Room", blank=True)

    def __str__(self):
        return self.name

    def count_rooms(self):
        return self.rooms.count()

    count_rooms.short_description = "Numbers of Room"
