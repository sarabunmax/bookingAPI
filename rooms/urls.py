from django.urls import path
from rooms.views import RoomListAPIView

app_name = 'rooms'

urlpatterns = [
    path('rooms-list/', RoomListAPIView.as_view(), name='rooms_list'),
]
