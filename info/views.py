from django.shortcuts import render, redirect
from django.views import View
from employee.models import Employee
from django.contrib import messages
from datetime import date,datetime, timedelta

# Create your views here.


class MainInfoView(View):
    def get(self, request):
        return render(request, "info/maininfo.html")
    

    
class IndexView(View):
    def time_converter(self, totalSeconds):
        hours, remainder = divmod(totalSeconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        sum_time = timedelta(hours=hours, minutes=minutes, seconds=seconds)
        result = "{:02}:{:02}".format(sum_time.seconds // 3600, (sum_time.seconds // 60) % 60)
        return result
        
    def get(self, request):
        return render(request, "info/month-report.html")
    
    def post(self, request):
        
        context = {}
        employee_today = []
        existing_user = False
        date_format = "%Y-%m"
        employees = Employee.objects.all()
        search_month = request.POST.get("search")
        get_civil = request.POST.get("civil")
        permit_number_month = 0
        format_string = "%H:%M"
        total_seconds = 0
        total_seconds_all_small_permissons = 0
        
        if search_month != ""and get_civil != "":
            search_value_time = datetime.strptime(search_month, date_format)
            get_month = search_value_time.date().month
            get_year = search_value_time.date().year
            for employee in employees:
                month = employee.created_date.month
                year = employee.created_date.year
                civil_id = employee.civil_id
                if month == get_month and year == get_year and civil_id == get_civil :

                    permission_duration_sum_all = employee.permission_duration_for_month_report()
                    permission_duration_sum_all_converting = datetime.strptime(permission_duration_sum_all, format_string).time()
                    total_seconds_all_small_permissons += (permission_duration_sum_all_converting.hour * 3600 + permission_duration_sum_all_converting.minute * 60 + permission_duration_sum_all_converting.second)

                    whole_permission_time = employee.whole_permission_duration_for_month()
                    whole_permission_time_converting = datetime.strptime(whole_permission_time, format_string).time()
                    total_seconds += (whole_permission_time_converting.hour * 3600 + whole_permission_time_converting.minute * 60 + whole_permission_time_converting.second)
                

                    if employee.permission_leaving_time.hour > 0:
                        permit_number_month += 1
                    if employee.permission_leaving_time_2.hour > 0:
                        permit_number_month += 1
                    if employee.permission_leaving_time_3.hour > 0:
                        permit_number_month += 1

                    employee_today.append(employee)
                    existing_user = True
                

            if not existing_user:
                 messages.error(request, "لا توجد نتائج بحث لهذا التاريخ والهوية المدنية")
        
        else:
            messages.error(request, "أدخل تاريخًا صحيحًا أو رقم هوية مدنية صحيحة")
        
        
        context["existing_user"] = existing_user
        context["employee_today"] = employee_today
        context["permit_number_month"] = permit_number_month
        context["result_time_for_whole_month_permissions"] = self.time_converter(totalSeconds=total_seconds)
        context["result_time_for_small_permissions"] = self.time_converter(totalSeconds=total_seconds_all_small_permissons)
        
        if len(employee_today) > 0:
            context["one_employee"] = employee_today[0]

        return render(request, "info/month-report.html", context)








class DialyReportView(View):
    def time_converter(self, totalSeconds):
        hours, remainder = divmod(totalSeconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        sum_time = timedelta(hours=hours, minutes=minutes, seconds=seconds)
        result = "{:02}:{:02}".format(sum_time.seconds // 3600, (sum_time.seconds // 60) % 60)
        return result
    
    def get(self, request):
        return render(request, "info/daily-report.html")
    

    def post(self, request):
        
        context = {}
        employee_today = []
        existing_user = False
        date_format = "%Y-%m-%d"
        employees = Employee.objects.all()
        search_date = request.POST.get("search")
        get_civil = request.POST.get("civil")
        permit_number_month = 0
        format_string = "%H:%M"
        total_seconds = 0
        total_seconds_all_small_permissons = 0

        
        if search_date != ""and get_civil != "":
            search_value_time = datetime.strptime(search_date, date_format)
            get_month = search_value_time.date().month
            get_year = search_value_time.date().year
            get_day = search_value_time.date().day

            for employee in employees:
                month = employee.created_date.month
                year = employee.created_date.year
                day = employee.created_date.day + 1
                civil_id = employee.civil_id
                if month == get_month and year == get_year and day == get_day and civil_id == get_civil :

                    permission_duration_sum_all = employee.permission_duration_for_month_report()
                    permission_duration_sum_all_converting = datetime.strptime(permission_duration_sum_all, format_string).time()
                    total_seconds_all_small_permissons += (permission_duration_sum_all_converting.hour * 3600 + permission_duration_sum_all_converting.minute * 60 + permission_duration_sum_all_converting.second)

                    whole_permission_time = employee.whole_permission_duration_for_month()
                    whole_permission_time_converting = datetime.strptime(whole_permission_time, format_string).time()
                    total_seconds += (whole_permission_time_converting.hour * 3600 + whole_permission_time_converting.minute * 60 + whole_permission_time_converting.second)
                

                    if employee.permission_leaving_time.hour > 0:
                        permit_number_month += 1
                    if employee.permission_leaving_time_2.hour > 0:
                        permit_number_month += 1
                    if employee.permission_leaving_time_3.hour > 0:
                        permit_number_month += 1

                    employee_today.append(employee)
                    existing_user = True
                

            if not existing_user:
                messages.error(request, "لا توجد نتائج بحث لهذا التاريخ والهوية المدنية")
        
        elif search_date != "":
            search_value_time = datetime.strptime(search_date, date_format)
            get_month = search_value_time.date().month
            get_year = search_value_time.date().year
            get_day = search_value_time.date().day

            for employee in employees:
                month = employee.created_date.month
                year = employee.created_date.year
                day = employee.created_date.day + 1
                civil_id = employee.civil_id
                if month == get_month and year == get_year and day == get_day:

                    permission_duration_sum_all = employee.permission_duration_for_month_report()
                    permission_duration_sum_all_converting = datetime.strptime(permission_duration_sum_all, format_string).time()
                    total_seconds_all_small_permissons += (permission_duration_sum_all_converting.hour * 3600 + permission_duration_sum_all_converting.minute * 60 + permission_duration_sum_all_converting.second)

                    whole_permission_time = employee.whole_permission_duration_for_month()
                    whole_permission_time_converting = datetime.strptime(whole_permission_time, format_string).time()
                    total_seconds += (whole_permission_time_converting.hour * 3600 + whole_permission_time_converting.minute * 60 + whole_permission_time_converting.second)
                

                    if employee.permission_leaving_time.hour > 0:
                        permit_number_month += 1
                    if employee.permission_leaving_time_2.hour > 0:
                        permit_number_month += 1
                    if employee.permission_leaving_time_3.hour > 0:
                        permit_number_month += 1

                    employee_today.append(employee)
                    existing_user = True
                

            if not existing_user:
                messages.error(request, "لا توجد نتائج بحث لهذا التاريخ")
        
        else:
            messages.error(request, "أدخل تاريخًا صحيحًا أو رقم هوية مدنية صحيحة")
        
        
        context["existing_user"] = existing_user
        context["employee_today"] = employee_today
        context["permit_number_month"] = permit_number_month
        context["result_time_for_whole_month_permissions"] = self.time_converter(totalSeconds=total_seconds)
        context["result_time_for_small_permissions"] = self.time_converter(totalSeconds=total_seconds_all_small_permissons)
        
        if len(employee_today) > 0:
            context["one_employee"] = employee_today[0]

        return render(request, "info/daily-report.html", context)