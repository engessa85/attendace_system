# Generated by Django 4.2.5 on 2023-09-12 23:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("employee", "0007_alter_employee_department_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sheet",
            name="created_date",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]