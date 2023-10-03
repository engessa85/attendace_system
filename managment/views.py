from django.shortcuts import render, redirect
from django.views import View
from employee.models import Employee, EmployeeEssentialInfo
from datetime import date,datetime
from django.http import JsonResponse



# Create your views here.

user_info = [{"name":"mohamed", "civil_id":1111}, {"name":"ahmed", "civil_id":2222}]
today = date.today()

# ## day of django time zone
# custom_day = today + timedelta(days=1)

class IndexView(View):
    def get(self, request):

        employee = Employee.objects.all()
        employee_today = Employee.objects.filter(created_date__date = today)
        
        if employee_today.exists():
            return render(request, "managment/index.html", context={"employee_today":employee_today, "date":today})
        else:
            return render(request, "managment/index.html")

    
    def post(self, request):
        for emp in EmployeeEssentialInfo.objects.all():
            Employee.objects.create(created_date = today , name = emp.name, civil_id = emp.civil_id, department = emp.department)
    
        return redirect("managment_index")
    

class UpdateView(View):
    def get(self,request, pk):
        employee = Employee.objects.get(pk=pk)
        id = employee.id
        name = employee.name
        created_date = today
        enterance_time = employee.enterance_time.strftime("%H:%M")
        final_leaving_time = employee.final_leaving_time.strftime("%H:%M")

        permission_leaving_time = employee.permission_leaving_time.strftime("%H:%M")
        permission_entering_time = employee.permission_entering_time.strftime("%H:%M")

        permission_leaving_time_2 = employee.permission_leaving_time_2.strftime("%H:%M")
        permission_entering_time_2 = employee.permission_entering_time_2.strftime("%H:%M")
        
        permission_leaving_time_3 = employee.permission_leaving_time_3.strftime("%H:%M")
        permission_entering_time_3 = employee.permission_entering_time_3.strftime("%H:%M")

        context = {"id":id, "name":name, "created_date":created_date,  "enterance_time":enterance_time, "final_leaving_time":final_leaving_time, "permission_leaving_time":permission_leaving_time, "permission_entering_time":permission_entering_time,
                  "permission_leaving_time_2":permission_leaving_time_2,"permission_entering_time_2":permission_entering_time_2,
                  "permission_leaving_time_3":permission_leaving_time_3, "permission_entering_time_3":permission_entering_time_3}
        return render(request, "managment/update.html", context)
    
    def post(self, request, pk):
        
        enter_time = request.POST.get("enter-time")
        enter_time_converted = datetime.strptime(enter_time, '%H:%M').time()

        final_leave_time = request.POST.get("final-leave-time")
        final_leave_time_converted = datetime.strptime(final_leave_time, '%H:%M').time()

        permission_leave_time_1 = request.POST.get("permission-leave-time-1")
        permission_leave_time_1_converted = datetime.strptime(permission_leave_time_1, '%H:%M').time()
        
        permission_enter_time_1 = request.POST.get("permission-enter-time-1")
        permission_enter_time_1_converted = datetime.strptime(permission_enter_time_1, '%H:%M').time()



        permission_leave_time_2 = request.POST.get("permission-leave-time-2")
        permission_leave_time_2_converted = datetime.strptime(permission_leave_time_2, '%H:%M').time()
        
        permission_enter_time_2 = request.POST.get("permission-enter-time-2")
        permission_enter_time_2_converted = datetime.strptime(permission_enter_time_2, '%H:%M').time()


        permission_leave_time_3 = request.POST.get("permission-leave-time-3")
        permission_leave_time_3_converted = datetime.strptime(permission_leave_time_3, '%H:%M').time()
        
        permission_enter_time_3 = request.POST.get("permission-enter-time-3")
        permission_enter_time_3_converted = datetime.strptime(permission_enter_time_3, '%H:%M').time()

        employee = Employee.objects.get(pk=pk)
        employee.enterance_time = enter_time_converted
        employee.final_leaving_time = final_leave_time_converted

        employee.permission_leaving_time = permission_leave_time_1_converted
        employee.permission_entering_time = permission_enter_time_1_converted

        employee.permission_leaving_time_2 = permission_leave_time_2_converted
        employee.permission_entering_time_2 = permission_enter_time_2_converted

        employee.permission_leaving_time_3 = permission_leave_time_3_converted
        employee.permission_entering_time_3 = permission_enter_time_3_converted

        employee.save()

        return redirect("managment_index")


        
def get_permmissions(request, pk):
    employee_today = Employee.objects.get(id = pk, created_date__date = today)
    data = {}

    data["permission_leaving_time"] = employee_today.permission_leaving_time
    data["permission_entering_time"] = employee_today.permission_entering_time

    data["permission_leaving_time_2"] = employee_today.permission_leaving_time_2
    data["permission_entering_time_2"] = employee_today.permission_entering_time_2

    data["permission_leaving_time_3"] = employee_today.permission_leaving_time_3
    data["permission_entering_time_3"] = employee_today.permission_entering_time_3

    return JsonResponse({"data":data}, safe=False)
    


