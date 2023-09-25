from django.contrib import admin
from reservations.models import Reservations

# Register your models here.


@admin.register(Reservations)
class ReservationsAdmin(admin.ModelAdmin):  # register model to admin panel
    list_display = ('id', 'room', 'user', 'date_time', 'duration')
