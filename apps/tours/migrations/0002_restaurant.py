# Generated by Django 5.0.7 on 2024-08-01 14:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tours", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Restaurant",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=250)),
                ("image", models.ImageField(upload_to="images/restaurants")),
                ("address", models.CharField(blank=True, max_length=500, null=True)),
                (
                    "destination",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="restaurants",
                        to="tours.destination",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
