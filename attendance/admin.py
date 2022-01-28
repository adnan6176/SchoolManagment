from django.contrib import admin

# Register your models here.
from . models import Student
from . models import Attendance

from . models import classID
from . models import Profile
from . models import TimeTable, DayName #, Customer ,Staff
# class AttendanceAdmin(admin.ModelAdmin):
#     readonly_fields =('submit_date')



admin.site.register(Student)
admin.site.register(Attendance)
admin.site.register(classID)
admin.site.register(Profile)
admin.site.register(TimeTable)
admin.site.register(DayName)
# admin.site.register(Customer)
# admin.site.register(Staff)
# admin.site.register(ContactInfo)

# admin.site.register(AttendanceAdmin)