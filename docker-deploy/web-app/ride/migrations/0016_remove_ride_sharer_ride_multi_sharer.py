# Generated by Django 4.1.5 on 2023-02-03 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ride", "0015_remove_ride_sharer_ride_sharer"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ride",
            name="sharer",
        ),
        migrations.AddField(
            model_name="ride",
            name="multi_sharer",
            field=models.ManyToManyField(to="ride.sharer"),
        ),
    ]
