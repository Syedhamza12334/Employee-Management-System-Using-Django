from django import forms
from .models import Employee,Project,Attendance

SKILL_CHOICES = [
    ("python", "python"),
    ("java", "java"),
    ("django", "django"),
    ("react", "react"),
    ("node", "node"),
    ("C++", "C++"),
]

class EmployeeForm(forms.ModelForm):
    skills = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=SKILL_CHOICES
    )

    class Meta:
        model = Employee
        fields = "__all__"
        labels = {"email": "Email ID", "mobile": "Mobile NO"}
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "gender": forms.Select(attrs={"class": "form-control"}),
            "state": forms.Select(attrs={"class": "form-control"}),
            "city": forms.TextInput(attrs={"class": "form-control"}),
            "profile_picture": forms.FileInput(attrs={"class": "form-control"}),
            "mobile": forms.NumberInput(attrs={"class": "form-control"}),
            "date_of_birth": forms.DateInput(attrs={"class": "form-control","id":"datepicker"}),
        }





class ProjectForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = "__all__"
        widgets = {
            "start_date": forms.DateInput(attrs={"class": "form-control","id":"datepicker"}),
            "end_date": forms.DateInput(attrs={"class": "form-control","id":"ENDDATE"}),
        }

    def __init__(self,*args, **kwargs):
            super(ProjectForm,self).__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['class']='form-control'



class AttendanceForm(forms.ModelForm):
    
    class Meta:
        model = Attendance
        fields = "__all__"
        widgets = {
            "date": forms.DateInput(attrs={"id":"datepicker"}),
        }

    def __init__(self,*args, **kwargs):
            super(AttendanceForm,self).__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['class']='form-control'


                

