from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path("",views.employee_list,name="employee_list"),
    path("details/<int:id>/",views.employee_detail,name="employee_detail"),
    path("employee_add/",views.employee_add,name="employee_add"),
    path("employee_update/<int:id>/",views.employee_update,name="employee_update"),
    path("delete_employee/<int:id>/",views.delete_employee,name="delete_employee"),
    path('projects/',views.project_list,name="project_list"),
    path("project_details/<int:id>/",views.project_details,name="project_details"),
    path('project_add/',views.project_add,name="project_add"),
   path('attendance_list/',views.attendance_list,name="attendance_list"),
   path("attendance_details/<int:id>/",views.attendance_details,name="attendance_details"),
    path('attendance_add/',views.attendance_add,name="attendance_add"),

    
   


]+ static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

