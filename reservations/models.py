from django.db import models
from django.utils.timezone import localdate, localtime
from core import models as core_models


class Reservation(core_models.TimeStampedModel):

    """ Reservation Model Defination """

    STATUS_CHOICES = (
        ("Pending", "Pending"),
        ("Confirmed", "Confirmed"),
        ("Canceled", "Canceled"),
    )

    status = models.CharField(choices=STATUS_CHOICES, max_length=10)
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.room}--{self.check_in}'

    def in_progress(self):
        inprogress = localdate()
        return inprogress > self.check_in and inprogress < self.check_out

    in_progress.boolean = True

    def is_finished(self):
        now = localdate()
        return now > self.check_out

    is_finished.boolean = True
