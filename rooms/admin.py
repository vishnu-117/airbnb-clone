from django.contrib import admin
from .models import Room, RoomType, Facility, Amenity, HouseRule, Photo
from django.utils.html import mark_safe
# Register your models here.


@admin.register(RoomType, Facility, Amenity, HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """Item Admin Defination """

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Defination """

    list_display = ('__str__', "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img src="{obj.file.url}" width="50px"/>')
    get_thumbnail.short_discription = "Thumbnail"


class PhotoInline(admin.TabularInline):
    model = Photo


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Defination """
    fieldsets = (
        (
            "Basic info", {"fields": ("name", "description", "country", "city", "address", "price")
                           }),
        (
            "Times", {"fields": ("check_in", "check_out", "instant_book")
                      }),
        (
            "More About the Spaces", {
                "classes": ("collapse",),
                "fields": ("aminities", "facility", "house_rules")
            }),
        (
            "Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")
                       }),
        (
            "Last Detal", {"fields": ("host",)
                           }),
    )
    list_display = ("name",
                    "country",
                    "city",
                    "price",
                    "address",
                    "guests",
                    "beds",
                    "bedrooms",
                    "baths",
                    "instant_book",
                    "count_aminities",
                    "count_photos",
                    "total_rating",
                    )
    ordering = ("name", "price")
    list_filter = ("instant_book",
                   "room_type",
                   "aminities",
                   "host__superhost",
                   "host__gender",
                   "facility",
                   "house_rules",
                   "city",
                   "country")
    filter_horizontal = (
        "aminities",
        "facility",
        "house_rules",
    )
    search_fields = ["city", "host__username"]
    raw_id_fields = ("host",)
    inlines = [PhotoInline, ]

    def count_aminities(self, obj):
        return obj.aminities.count()
    count_aminities.short_description = "Total Aminity"

    def count_photos(self, obj):
        return obj.photos.count()
