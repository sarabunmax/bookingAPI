from django.contrib import admin
from rooms.models import Rooms

# Register your models here.


@admin.register(Rooms)
class RoomsAdmin(admin.ModelAdmin):  # register model to admin panel
    list_display = ('id', 'type', 'status')
