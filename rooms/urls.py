from django.urls import path
from .views import RoomDetail, SearchView

app_name = "rooms"

urlpatterns = [
    path('<int:pk>', RoomDetail.as_view(), name="room_detail"),
    path('search/', SearchView.as_view(), name="search"),
]
