from django.shortcuts import render ,get_object_or_404,HttpResponseRedirect,redirect
from . models import Employee,Project,Attendance
from . forms import EmployeeForm,ProjectForm,AttendanceForm

# Create your views here.


def employee_list(request):
    employees=Employee.objects.all()
    return render(request,"employee_list.html",{'employees':employees})

def employee_detail(request,id):
    employee=get_object_or_404(Employee,id=id)
    return render(request,"employee_detail.html",{"employee":employee})  

def employee_add(request):
    if request.method=="POST":
        form=EmployeeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:        
        form =EmployeeForm()
    return render (request,"employee_add.html",{"form":form})    


def employee_update(request,id):
    employee=get_object_or_404(Employee,id=id)
    if request.method=="POST":
        form=EmployeeForm(request.POST,request.FILES,instance=employee)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        initial_skills=[skill.strip(" '[]") for skill in employee.skills.split(",")]
        form=EmployeeForm(instance=employee,initial={'skills':initial_skills}) 
    return render(request,"employee_update.html",{"form":form})     

def delete_employee(request,id):
    employee=get_object_or_404(Employee,id=id)
    employee.delete()
    return redirect("employee_list")  

def project_list(request):
    projects=Project.objects.all()
    return render(request,"project_list.html",{'projects':projects})

def project_details(request,id):
    project=get_object_or_404(Project,id=id)
    return render(request,"project_details.html",{"project":project})    




def project_add(request):
    if request.method=="POST":
        form=ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("project_list")  
    else:        
        form =ProjectForm()
    return render (request,"project_add.html",{"form":form})   



def attendance_list(request):
    attendance=Attendance.objects.all()
    return render(request,"attendance_list.html",{'attendances':attendance})



def attendance_details(request,id):
    attendance=get_object_or_404(Attendance,id=id)
    return render(request,"attendance_details.html",{"attendances":attendance})    


def attendance_add(request):
    if request.method=="POST":
        form=AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("attendance_list")  
    else:        
        form =AttendanceForm()
    return render (request,"attendance_add.html",{"form":form})   


