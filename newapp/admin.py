from django.contrib import admin
from . models import Employee, Project,Attendance

# Register your models here.


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['name','email','mobile','date_of_birth','gender','skills','state','city','profile_picture','resume','video']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display=['id','title','description','start_date','end_date','employees_assigned_list']
    def employees_assigned_list(self,obj):
        return ", ".join([employee.name for employee in obj.employees_assigned.all()])
    employees_assigned_list.short_description ='Employee Assigned' 

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display=['id','date','employee','status']
    
    
