from django.db import models
from rooms.models import Rooms
from django.contrib.auth.models import User


class Reservations(models.Model):  # model for saving information about reservations in DataBase
    room = models.ForeignKey(to=Rooms, on_delete=models.PROTECT)  # reserved room
    user = models.ForeignKey(to=User, on_delete=models.PROTECT)  # who reserved room
    date_time = models.DateTimeField(null=True)  # date and time reservation
    duration = models.IntegerField(null=True)  # duration reservation
