from django.contrib import admin
from .models import Employee, EmployeeEssentialInfo

# Register your models here.

admin.site.register(Employee)
admin.site.register(EmployeeEssentialInfo)

