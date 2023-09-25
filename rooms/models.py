from django.db import models


class Rooms(models.Model):  # model for saving information about rooms in DataBase
    type = models.CharField(max_length=5)  # type of room (big or small)
    status = models.CharField(max_length=8)  # current status of room (free or reserved)
