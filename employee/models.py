from django.db import models
from datetime import time, datetime, timedelta
from datetime import date, timedelta
from django.utils import timezone



today = date.today()
custom_day = today + timedelta(days=1)

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=300, null=True, blank=True)
    civil_id = models.CharField(max_length=300, null=True, blank=True)
    department = models.CharField(default="ELectrical Dep",max_length=300, null=True, blank=True)
    enterance_time = models.TimeField(default=time(0,0) , null=True, blank=True)

    permission_leaving_time = models.TimeField(default=time(0,0), null=True, blank=True)
    permission_entering_time = models.TimeField(default=time(0,0), null=True, blank=True)
    is_permit_private_1 = models.BooleanField(default=True, null=True, blank=True)
    is_permit_hospital_1 = models.BooleanField(default=False, null=True, blank=True)
    is_permit_official_1 = models.BooleanField(default=False, null=True, blank=True)

    permission_leaving_time_2 = models.TimeField(default=time(0,0), null=True, blank=True)
    permission_entering_time_2 = models.TimeField(default=time(0,0), null=True, blank=True)
    is_permit_private_2 = models.BooleanField(default=True, null=True, blank=True)
    is_permit_hospital_2 = models.BooleanField(default=False, null=True, blank=True)
    is_permit_official_2 = models.BooleanField(default=False, null=True, blank=True)
    

    permission_leaving_time_3 = models.TimeField(default=time(0,0), null=True, blank=True)
    permission_entering_time_3 = models.TimeField(default=time(0,0), null=True, blank=True)
    is_permit_private_3 = models.BooleanField(default=True, null=True, blank=True)
    is_permit_hospital_3 = models.BooleanField(default=False, null=True, blank=True)
    is_permit_official_3 = models.BooleanField(default=False, null=True, blank=True)

    final_leaving_time = models.TimeField(default=time(0,0),null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.name) + ' / ' + str(self.created_date.date() + timedelta(days=1))

    def calculate_morning_delay_time(self):
        if self.enterance_time > time(8,30):
            datetime1 = datetime.combine(datetime.today(), self.enterance_time)
            datetime2 = datetime.combine(datetime.today(), time(8, 30))
            time_difference = datetime1 - datetime2

            hours, remainder = divmod(time_difference.seconds, 3600)
            minutes, _ = divmod(remainder, 60)
            formatted_time = f'{hours:02}:{minutes:02}'
            return formatted_time
        else:
            return "00:00"
    
    def expected_leaving_time(self):

        if self.enterance_time == time(0,0):
            return "00:00"

        elif self.enterance_time <= time(8):
            return "14:30"
        
        elif self.enterance_time > time(8):
            official_leaving_time = datetime.combine(datetime.today(), time(14, 30))
            datetime1 = datetime.combine(datetime.today(), time(8))
            datetime2 = datetime.combine(datetime.today(), self.enterance_time)
            time_difference = datetime2 - datetime1
            final_time = official_leaving_time + time_difference
            final_hour = final_time.hour
            final_minute = final_time.minute

            if final_hour > 15:
                formatted_time = f'{15:02}:{00:02}'
            else:
                formatted_time = f'{final_hour:02}:{final_minute:02}'
            return formatted_time
    

    def permission_duration(self):
        permit1_datetime1 = datetime.combine(datetime.today(), self.permission_entering_time)
        permit1_datetime2 = datetime.combine(datetime.today(), self.permission_leaving_time)

        if self.is_permit_private_1 == True:
            time_difference_1 = permit1_datetime1 - permit1_datetime2
        else:
            time_difference_1 = timedelta(hours=0, minutes=0)
        
    

        permit2_datetime1 = datetime.combine(datetime.today(), self.permission_entering_time_2)
        permit2_datetime2 = datetime.combine(datetime.today(), self.permission_leaving_time_2)

        if self.is_permit_private_2 == True:
            time_difference_2 = permit2_datetime1 - permit2_datetime2
        else:
            time_difference_2 = timedelta(hours=0, minutes=0)


        permit3_datetime1 = datetime.combine(datetime.today(), self.permission_entering_time_3)
        permit3_datetime2 = datetime.combine(datetime.today(), self.permission_leaving_time_3)

        if self.is_permit_private_3 == True:
            time_difference_3 = permit3_datetime1 - permit3_datetime2
        else:
            time_difference_3 = timedelta(hours=0, minutes=0)


        total = time_difference_1 + time_difference_2 + time_difference_3

        hours, remainder = divmod(total.seconds, 3600)
        minutes, _ = divmod(remainder, 60)
        formatted_time = f'{hours:02}:{minutes:02}'
        

        return formatted_time
    

    def permission_duration_for_month_report(self):
        permit1_datetime1 = datetime.combine(datetime.today(), self.permission_entering_time)
        permit1_datetime2 = datetime.combine(datetime.today(), self.permission_leaving_time)
        time_difference_1 = permit1_datetime1 - permit1_datetime2


        permit2_datetime1 = datetime.combine(datetime.today(), self.permission_entering_time_2)
        permit2_datetime2 = datetime.combine(datetime.today(), self.permission_leaving_time_2)
        time_difference_2 = permit2_datetime1 - permit2_datetime2


        permit3_datetime1 = datetime.combine(datetime.today(), self.permission_entering_time_3)
        permit3_datetime2 = datetime.combine(datetime.today(), self.permission_leaving_time_3)
        time_difference_3 = permit3_datetime1 - permit3_datetime2


        total = time_difference_1 + time_difference_2 + time_difference_3

        hours, remainder = divmod(total.seconds, 3600)
        minutes, _ = divmod(remainder, 60)
        formatted_time = f'{hours:02}:{minutes:02}'
    
        return formatted_time
    
    def early_leaving_time(self):
        time_difference = timedelta(hours=0, minutes=0)
        format_string = "%H:%M"
        h_expecting_time = datetime.strptime(self.expected_leaving_time(), format_string).time()
        i_final_leaving_time = self.final_leaving_time

        if i_final_leaving_time <= time(15,0):
            if i_final_leaving_time == time(0,0):
                time_difference = timedelta(hours=0, minutes=0)
            elif i_final_leaving_time <= time(14,30):
                time_difference = datetime.combine(datetime.today(), h_expecting_time) - datetime.combine(datetime.today(), i_final_leaving_time)
            elif i_final_leaving_time  >= h_expecting_time:
                time_difference = timedelta(hours=0, minutes=0)
            else:
                time_difference = datetime.combine(datetime.today(), h_expecting_time) - datetime.combine(datetime.today(), i_final_leaving_time)
        
        else:
            time_difference = timedelta(hours=0, minutes=0)
        
        result_time = "{:02}:{:02}".format(time_difference.seconds // 3600, (time_difference.seconds // 60) % 60)
        
        return(result_time)
    
    def whole_permission_duration(self):

        format_string = "%H:%M"
        delay_morning= datetime.strptime(self.calculate_morning_delay_time(), format_string).time()
        permission_duration = datetime.strptime(self.permission_duration(), format_string).time()
        early_leaving = datetime.strptime(self.early_leaving_time(), format_string).time()

        total_seconds = delay_morning.hour * 3600 + delay_morning.minute * 60 + delay_morning.second + \
                permission_duration.hour * 3600 + permission_duration.minute * 60 + permission_duration.second + \
                early_leaving.hour * 3600 + early_leaving.minute * 60 + early_leaving.second

        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        sum_time = timedelta(hours=hours, minutes=minutes, seconds=seconds)
        
        result_time = "{:02}:{:02}".format(sum_time.seconds // 3600, (sum_time.seconds // 60) % 60)

        return result_time
    
    def staying_in_job_duration(self):
        format_string = "%H:%M"

        enterance_time_value = datetime.combine(datetime.today(), self.enterance_time)
        final_leaving_time = datetime.combine(datetime.today(), self.final_leaving_time)

        permission_duration_str = self.permission_duration()
        permission_duration_parts = permission_duration_str.split(":")
        permission_duration_timedelta = timedelta(hours=int(permission_duration_parts[0]), minutes=int(permission_duration_parts[1]))

        if self.enterance_time >= time(8, 0):
            if self.final_leaving_time <= time(15, 0):
                final_leaving_time = datetime.combine(datetime.today(), self.final_leaving_time)  # Convert to datetime
                time_diff = final_leaving_time - enterance_time_value - permission_duration_timedelta
            else:
                time_diff = datetime.combine(datetime.today(), time(15, 0)) - enterance_time_value - permission_duration_timedelta
        elif self.enterance_time == time(0,0) and self.final_leaving_time == time(0,0):
            time_diff = timedelta(hours=0, minutes=0)
        else:
            time_diff = datetime.combine(datetime.today(), time(15, 0)) - datetime.combine(datetime.today(), time(8, 0)) - permission_duration_timedelta

        
        result_time = "{:02}:{:02}".format(time_diff.seconds // 3600, (time_diff.seconds // 60) % 60)

        return result_time
    
    def staying_condition(self):
        status = ""
        format_string = "%H:%M"
        staying_in_work= datetime.strptime(self.staying_in_job_duration(), format_string).time()
        if staying_in_work >= time(5,0):
            status = "حاضر"
        else:
            status = "لم يكمل عدد الساعات"

        return status

        
        
        








    

    

