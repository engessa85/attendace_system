# Generated by Django 4.2.5 on 2023-09-12 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
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
                ("name", models.CharField(blank=True, max_length=300, null=True)),
                ("civil_id", models.CharField(blank=True, max_length=300, null=True)),
                ("department", models.CharField(blank=True, max_length=300, null=True)),
                ("enterance_time", models.TimeField(blank=True, null=True)),
            ],
        ),
    ]