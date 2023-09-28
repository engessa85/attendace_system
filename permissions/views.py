from django.shortcuts import render, redirect
from django.views import View
from employee.models import Employee
from datetime import datetime
from django.contrib import messages
from datetime import date,datetime

# Create your views here.
today = date.today()

class IndexView(View):
    def get(self, request):
        return render(request, "permissions/index.html")
    def post(self, request):
        context = {}
        date_format = "%Y-%m-%d"
        search_value = request.POST.get("search")
        employees = Employee.objects.all()
        employee_today = []
        existing_user = False
        if search_value != "":
            search_value_time = datetime.strptime(search_value, date_format)
            get_month = search_value_time.date().month
            get_year = search_value_time.date().year
            get_day = search_value_time.date().day
            for employee in employees:
                month = employee.created_date.month
                year = employee.created_date.year
                day = employee.created_date.day + 1
                if month == get_month and year == get_year and day == get_day:
                    employee_today.append(employee)
                    existing_user = True
            if not existing_user:
                messages.error(request, "Employees are not existed in this date !!!")
        else:
            messages.error(request, "Invalid Date !!!")
        context["existing_user"] = existing_user
        context["employee_today"] = employee_today
        return render(request, "permissions/index.html", context)




class UpdateView(View):
    def get(self,request, pk):
        employee = Employee.objects.get(pk=pk)
        id = employee.id
        name = employee.name
        created_date = employee.created_date

        permission_leaving_time = employee.permission_leaving_time.strftime("%H:%M")
        permission_entering_time = employee.permission_entering_time.strftime("%H:%M")
        is_permit_private_1 = employee.is_permit_private_1
        is_permit_hospital_1 = employee.is_permit_hospital_1
        is_permit_official_1 = employee.is_permit_official_1

        permission_leaving_time_2 = employee.permission_leaving_time_2.strftime("%H:%M")
        permission_entering_time_2 = employee.permission_entering_time_2.strftime("%H:%M")
        is_permit_private_2 = employee.is_permit_private_2
        is_permit_hospital_2 = employee.is_permit_hospital_2
        is_permit_official_2 = employee.is_permit_official_2
        
        permission_leaving_time_3 = employee.permission_leaving_time_3.strftime("%H:%M")
        permission_entering_time_3 = employee.permission_entering_time_3.strftime("%H:%M")
        is_permit_private_3 = employee.is_permit_private_3
        is_permit_hospital_3 = employee.is_permit_hospital_3
        is_permit_official_3 = employee.is_permit_official_3

        context = {"id":id, "name":name, "created_date":created_date,   "permission_leaving_time":permission_leaving_time, "permission_entering_time":permission_entering_time,
                  "permission_leaving_time_2":permission_leaving_time_2,"permission_entering_time_2":permission_entering_time_2,
                  "permission_leaving_time_3":permission_leaving_time_3, "permission_entering_time_3":permission_entering_time_3,
                  "is_permit_private_1":is_permit_private_1, "is_permit_hospital_1":is_permit_hospital_1, "is_permit_official_1":is_permit_official_1,
                  "is_permit_private_2":is_permit_private_2, "is_permit_hospital_2":is_permit_hospital_2, "is_permit_official_2":is_permit_official_2,
                   "is_permit_private_3":is_permit_private_3, "is_permit_hospital_3":is_permit_hospital_3, "is_permit_official_3":is_permit_official_3 }
        
        
        return render(request, "permissions/update.html", context)
    
    def post(self, request, pk):
        
        print(pk)

        get_private1 = request.POST.get("private1")
        get_hospital1 = request.POST.get("hospital1")
        get_official1 = request.POST.get("official1")

        get_private2 = request.POST.get("private2")
        get_hospital2 = request.POST.get("hospital2")
        get_official2 = request.POST.get("official2")

        get_private3 = request.POST.get("private3")
        get_hospital3 = request.POST.get("hospital3")
        get_official3 = request.POST.get("official3")
        
        
        employee = Employee.objects.get(pk=pk)
        

        employee.is_permit_private_1 = bool(get_private1)
        employee.is_permit_hospital_1 = bool(get_hospital1)
        employee.is_permit_official_1 = bool(get_official1)

        employee.is_permit_private_2 = bool(get_private2)
        employee.is_permit_hospital_2 = bool(get_hospital2)
        employee.is_permit_official_2 = bool(get_official2)

        employee.is_permit_private_3 = bool(get_private3)
        employee.is_permit_hospital_3 = bool(get_hospital3)
        employee.is_permit_official_3 = bool(get_official3)

        employee.save()
        messages.success(request, "Permissions are updated successfully")

        return redirect("permissions_index")