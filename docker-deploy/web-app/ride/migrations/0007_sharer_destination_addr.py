# Generated by Django 4.1.5 on 2023-02-02 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ride", "0006_alter_driver_vehicle_type_alter_ride_special_request_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="sharer",
            name="destination_addr",
            field=models.CharField(default="Duke", max_length=20),
        ),
    ]
