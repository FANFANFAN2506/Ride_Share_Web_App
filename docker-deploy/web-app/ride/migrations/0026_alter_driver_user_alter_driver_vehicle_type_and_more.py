# Generated by Django 4.1.5 on 2023-02-05 02:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("ride", "0025_alter_sharer_ride_joined"),
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
        migrations.AlterField(
            model_name="driver",
            name="vehicle_type",
            field=models.CharField(
                choices=[("economy", "economy"), ("luxury", "luxury")],
                default="economy",
                help_text="Vehicle type",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="ride",
            name="owner",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
