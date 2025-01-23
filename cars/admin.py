from django.contrib import admin
from cars.models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["id", "model", "transmission", "airConditioning",
                    "pricePerHour", "fuelType", "builtIn"]
    list_display_links = ["model"]
    list_editable = ["airConditioning", "builtIn"]