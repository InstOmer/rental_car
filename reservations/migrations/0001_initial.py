# Generated by Django 5.1.5 on 2025-01-21 18:19

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("cars", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Reservation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("pickUpTime", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "dropOffTime",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("pickUpLocation", models.CharField(max_length=150)),
                ("dropOffLocation", models.CharField(max_length=150)),
                ("status", models.CharField(default="CREATED", max_length=20)),
                ("totalPrice", models.DecimalField(decimal_places=2, max_digits=20)),
                (
                    "car",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cars.car"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
