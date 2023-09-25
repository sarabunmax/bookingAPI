from rest_framework import serializers
from reservations.models import Reservations


class ReservationSerializer(serializers.ModelSerializer):  # class serializer for paking data to JSON
    class Meta:
        model = Reservations
        fields = ('id', 'room', 'user', 'date_time', 'duration')
