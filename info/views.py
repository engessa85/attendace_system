from django.shortcuts import render, redirect
from django.views import View
from employee.models import Employee
from django.contrib import messages
from datetime import date,datetime, timedelta

# Create your views here.


class IndexView(View):
    def get(self, request):
        return render(request, "info/index.html")
    
    def post(self, request):
        
        context = {}
        employee_today = []
        existing_user = False
        date_format = "%Y-%m"
        employees = Employee.objects.all()
        search_month = request.POST.get("search")
        get_civil = request.POST.get("civil")




        if search_month != ""and get_civil != "":
            search_value_time = datetime.strptime(search_month, date_format)
            get_month = search_value_time.date().month
            get_year = search_value_time.date().year
            for employee in employees:
                month = employee.created_date.month
                year = employee.created_date.year
                civil_id = employee.civil_id
                if month == get_month and year == get_year and civil_id == get_civil :
                    print(employee.created_date)
                    employee_today.append(employee)
                    existing_user = True
                

            if not existing_user:
                messages.error(request, "Search results for this date and civil id not existed !!!")
        
        
        elif search_month != "":
            search_value_time = datetime.strptime(search_month, date_format)
            get_month = search_value_time.date().month
            get_year = search_value_time.date().year
            
            for employee in employees:
                month = employee.created_date.month
                year = employee.created_date.year
                if month == get_month and year == get_year:
                    employee_today.append(employee)
                    existing_user = True

            if not existing_user:
                messages.error(request, "Employees are not existed in this date !!!")
        
        elif get_civil != "":
            for employee in employees:
                if get_civil == employee.civil_id:
                    employee_today.append(employee)
                    existing_user = True

            if not existing_user:
                messages.error(request, "Employee with this civil id is not existed !!!")
        
        else:
            messages.error(request, "Search by date or civil id !!!")
        
        
        context["existing_user"] = existing_user
        context["employee_today"] = employee_today
        

        
       
        
        return render(request, "info/index.html", context)
