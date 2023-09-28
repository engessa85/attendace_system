from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Employee, Sheet


# @receiver(post_save, sender = Sheet)
# def create_employee(sender, instance, created, **kwargs):
#     if created:
#         employee = Employee.objects.create(Sheet = instance) 
#         instance.employee = employee
#         instance.save()
