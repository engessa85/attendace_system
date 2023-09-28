# Generated by Django 4.2.5 on 2023-09-12 11:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("employee", "0002_employee_leaving_time_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="enterance_time",
            field=models.TimeField(blank=True, default=datetime.time(8, 30), null=True),
        ),
        migrations.AlterField(
            model_name="employee",
            name="leaving_time",
            field=models.TimeField(
                blank=True, default=datetime.time(15, 30), null=True
            ),
        ),
    ]