from django.db import models

# Create your models here





class Employee(models.Model):
    GENDER_CHOICES=[
        {"male","Male"},
        {"female","Female"},
        {"other","Other"}
    ]
    
    STATE_CHOICES=[
        ("AL", "Alabama"),
        ("AK", "Alaska"),
        ("AZ", "Arizona"),
        ("AR", "Arkansas"),
        ("CA", "California"),
        ("CO", "Colorado"),
        ("CT", "Connecticut"),
        ("DE", "Delaware"),
        ("FL", "Florida"),
        ("GA", "Georgia"),
        ("HI", "Hawaii"),
        ("ID", "Idaho"),
        ("IL", "Illinois"),
        ("IN", "Indiana"),
        ("IA", "Iowa"),
        ("KS", "Kansas"),
        ("KY", "Kentucky"),
        ("LA", "Louisiana"),
        ("ME", "Maine"),
        ("MD", "Maryland"),
        ("MA", "Massachusetts"),
        ("MI", "Michigan"),
        ("MN", "Minnesota"),
        ("MS", "Mississippi"),
        ("MO", "Missouri"),
        ("MT", "Montana"),
        ("NE", "Nebraska"),
        ("NV", "Nevada"),
        ("NH", "New Hampshire"),
        ("NJ", "New Jersey"),
        ("NM", "New Mexico"),
        ("NY", "New York"),
        ("NC", "North Carolina"),
        ("ND", "North Dakota"),
        ("OH", "Ohio"),
        ("OK", "Oklahoma"),
        ("OR", "Oregon"),
        ("PA", "Pennsylvania"),
        ("RI", "Rhode Island"),
        ("SC", "South Carolina"),
        ("SD", "South Dakota"),
        ("TN", "Tennessee"),
        ("TX", "Texas"),
        ("UT", "Utah"),
        ("VT", "Vermont"),
        ("VA", "Virginia"),
        ("WA", "Washington"),
        ("WV", "West Virginia"),
        ("WI", "Wisconsin"),
        ("WY", "Wyoming")
    ]


    name=models.CharField(max_length=255)
    email=models.EmailField()
    mobile=models.PositiveIntegerField()
    date_of_birth=models.DateField(auto_now_add=False,auto_now=False,null=True)
    gender=models.CharField(max_length=25,choices=GENDER_CHOICES,default='others')
    skills=models.CharField(max_length=100)
    state=models.CharField(max_length=100,choices=STATE_CHOICES)
    city=models.CharField(max_length=100) 
    profile_picture=models.ImageField(upload_to="employee_profile_picture/",null=True,blank=True)
    resume=models.FileField(upload_to="employee_resume/",null=True,blank=True)
    video=models.FileField(upload_to="employee_video/",blank=True)


    def __str__(self):
        return self.name


class Project(models.Model):
    title=models.CharField(max_length=255,default=None)
    description = models.TextField(default='No description provided')
    start_date=models.DateField(auto_now=False,auto_now_add=False,default=None)  
    end_date=models.DateField(auto_now=False,auto_now_add=False,default=None)
    employees_assigned=models.ManyToManyField(Employee) 




    def __str__(self):
        return 
    

class Attendance(models.Model):
    STATUS_CHOICES=[
        {'present','Present'},
        {'absent','Absent'},
        {'late','Late'},
    ]
    date=models.DateField(auto_now=False,auto_now_add=False,default=None)  
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES)
           
 
