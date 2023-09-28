# Generated by Django 4.2.5 on 2023-09-18 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("employee", "0018_alter_employee_created_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="employee",
            name="is_permit_hospital_1",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name="employee",
            name="is_permit_hospital_2",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name="employee",
            name="is_permit_hospital_3",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name="employee",
            name="is_permit_private_1",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name="employee",
            name="is_permit_private_2",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name="employee",
            name="is_permit_private_3",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]