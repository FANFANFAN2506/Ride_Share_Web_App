# Generated by Django 4.1.5 on 2023-02-04 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("ride", "0022_remove_sharer_ride_sharer_ride_unique_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="sharer",
            name="ride_unique_id",
        ),
        migrations.AddField(
            model_name="sharer",
            name="ride_joined",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="ride.ride",
            ),
        ),
    ]
