# Generated by Django 4.2.5 on 2023-09-11 17:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("taxi", "0002_alter_driver_options_alter_car_drivers_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="car",
            options={"ordering": ("model",)},
        ),
        migrations.AlterField(
            model_name="car",
            name="drivers",
            field=models.ManyToManyField(
                related_name="cars", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="car",
            name="manufacturer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cars",
                to="taxi.manufacturer",
            ),
        ),
    ]