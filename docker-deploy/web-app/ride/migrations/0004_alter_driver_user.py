# Generated by Django 4.1.5 on 2023-02-01 03:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("ride", "0003_ride_sharer_driver_user_driver_vehicle_type_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="driver",
            name="user",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
