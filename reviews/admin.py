from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    """ Review Admin Model """

    list_display = ("__str__", "rating_average")
