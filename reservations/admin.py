from django.contrib import admin
from reservations.models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ["id", "car", "user", "pickUpTime",
                    "dropOffTime", "pickUpLocation",
                    "dropOffLocation", "status", "totalPrice"]
    list_display_links = ["car"]