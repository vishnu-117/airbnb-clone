from django.contrib import admin
from .models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):

    """ Reservation Admin Defination """

    list_display = ("room", "status", "check_in",
                    "check_out", "guest", "in_progress", "is_finished")
    list_filter = ("status",)
