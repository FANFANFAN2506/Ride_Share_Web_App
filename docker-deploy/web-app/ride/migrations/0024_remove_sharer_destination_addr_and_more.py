# Generated by Django 4.1.5 on 2023-02-04 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ride", "0023_remove_sharer_ride_unique_id_sharer_ride_joined"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="sharer",
            name="destination_addr",
        ),
        migrations.RemoveField(
            model_name="sharer",
            name="earliest_date",
        ),
        migrations.RemoveField(
            model_name="sharer",
            name="latest_date",
        ),
    ]
