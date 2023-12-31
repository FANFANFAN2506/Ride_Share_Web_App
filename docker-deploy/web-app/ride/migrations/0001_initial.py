# Generated by Django 4.1.5 on 2023-01-31 21:10

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Driver",
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
                (
                    "liscense_plate",
                    models.CharField(
                        help_text="Enter your liscense plate", max_length=7, unique=True
                    ),
                ),
                ("max_num_passengers", models.IntegerField()),
                (
                    "special_request",
                    models.TextField(
                        blank=True, help_text="Enter a special request", max_length=1000
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Owner",
            fields=[
                (
                    "user_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "ride_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        help_text="Unique ID for the ride",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("destination_addr", models.CharField(max_length=200)),
                ("arrival_date", models.DateTimeField()),
                ("passenger_num", models.IntegerField(max_length=10)),
                (
                    "vehicle_type",
                    models.CharField(
                        choices=[
                            ("s", "SEDAN"),
                            ("c", "COUPE"),
                            ("w", "STATION WAGON"),
                        ],
                        default="s",
                        help_text="Vehicle type",
                        max_length=1,
                    ),
                ),
                (
                    "special_request",
                    models.TextField(
                        blank=True, help_text="Enter a special request", max_length=1000
                    ),
                ),
                ("if_share", models.BooleanField(default=False)),
                (
                    "status",
                    models.CharField(
                        choices=[("o", "open"), ("c", "confirmed"), ("f", "complete")],
                        default="o",
                        help_text="Ride status",
                        max_length=1,
                    ),
                ),
                (
                    "driver",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="ride.driver",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            bases=("auth.user",),
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
