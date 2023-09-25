from reservations.models import Reservations
from django.contrib.auth.models import User
from reservations.serializers import ReservationSerializer
# from rest_framework.generics import RetrieveDestroyAPIView, ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from datetime import datetime
from datetime import datetime, timedelta
import pytz
# Create your views here.


class ReservationAPIViewSet(ModelViewSet):
    # queryset = Reservations.objects.all()
    serializer_class = ReservationSerializer

    def get_queryset(self):  # overiding 'get_queryset' method for acces restrictions for ordinary users

        if self.action == 'list':
            username = self.request.user
            user = User.objects.get(username=username)
            if user.is_staff is True:
                return Reservations.objects.all()
            else:
                return Reservations.objects.filter(user=user.id)

    def create(self, request, *args, **kwargs):
        request_data = request.data  # data from HTTP request
        #  filtering exists reservations for booking date
        exists_reservations = Reservations.objects.filter(room_id=request_data['room'], date_time__date=datetime.strptime(request_data['date_time'], '%Y-%m-%d %H:%M:%S').date()).values('date_time', 'duration')
        utc = pytz.UTC  # UTC object for configuration timezone in datatime objects
        if exists_reservations.exists():

            # checking each reservation for coincidence
            for r in exists_reservations:
                duration = r['duration']

                # work with datetime variables
                exists_time_start = r['date_time']
                exists_time_end = exists_time_start + timedelta(minutes=duration)
                request_time_start = datetime.strptime(request_data['date_time'],  '%Y-%m-%d %H:%M:%S')
                request_time_end = request_time_start + timedelta(minutes=float(request_data['duration']))

                exists_time_start = exists_time_start.replace(tzinfo=utc)
                exists_time_end = exists_time_end.replace(tzinfo=utc)
                request_time_start = request_time_start.replace(tzinfo=utc)
                request_time_end = request_time_end.replace(tzinfo=utc)

                # matching condition
                if (exists_time_start <= request_time_end) and (request_time_start >= exists_time_end):
                    return Response({'success': 'REQUEST TIME IS BUSY !'}, status=400)
        else:
            super().create(request, *args, **kwargs)
            return Response({'success': 'SUCCESSFUL!'}, status=200)


