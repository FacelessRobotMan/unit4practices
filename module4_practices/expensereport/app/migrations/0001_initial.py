# Generated by Django 4.1.5 on 2023-02-02 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ExpenseTracker",
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
                ("date", models.DateField()),
                ("location", models.TextField()),
                ("amount", models.FloatField()),
                ("notes", models.TextField(blank=True)),
            ],
        ),
    ]
