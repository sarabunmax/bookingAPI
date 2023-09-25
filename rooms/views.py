from rest_framework.generics import ListAPIView
from rooms.models import Rooms
from django.contrib.auth.models import User
from rooms.serializers import RoomSerializer


class RoomListAPIView(ListAPIView):  # controler for hadling http request
    # queryset = Rooms.objects.all()  # list of query, that return data from data base
    serializer_class = RoomSerializer   # serializer for paking data to JSON

    def get_queryset(self):  # overiding 'get_queryset' method for acces restrictions for ordinary users
        user = self.request.user
        if User.objects.get(username=user).is_staff is True:
            return Rooms.objects.all()
        else:
            return Rooms.objects.filter(type='small')



