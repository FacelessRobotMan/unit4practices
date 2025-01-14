# Generated by Django 4.1.5 on 2023-02-04 17:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="leaverequest",
            name="approved_by",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="leaverequest",
            name="date_requested",
            field=models.DateTimeField(
                blank=True, default=datetime.datetime.today, null=True
            ),
        ),
        migrations.AlterField(
            model_name="leaverequest",
            name="notes",
            field=models.TextField(blank=True, null=True),
        ),
    ]
