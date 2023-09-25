from rest_framework import serializers
from rooms.models import Rooms


class RoomSerializer(serializers.ModelSerializer):  # class serializer for paking data to JSON
    class Meta:
        model = Rooms
        fields = ('id', 'type', 'status')
