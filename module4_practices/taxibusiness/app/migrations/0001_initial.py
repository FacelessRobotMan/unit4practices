# Generated by Django 4.1.5 on 2023-02-03 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TaxiBusiness",
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
                ("occupied", models.BooleanField()),
                ("capacity", models.IntegerField()),
                ("passengers", models.IntegerField()),
                ("fare", models.FloatField()),
                ("taxi_number", models.IntegerField(default=111)),
                ("notes", models.TextField(blank=True)),
            ],
        ),
    ]