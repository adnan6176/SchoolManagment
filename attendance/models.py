from distutils.command.upload import upload
from email.policy import default
from tokenize import blank_re
from django.db import models
from django.db.models.fields import BooleanField, CharField
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class classID(models.Model):
    classCode = models.CharField(max_length=2,blank=True, null=True)
    className = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        str_name =  self.className  
        return str_name


class Student(models.Model):
    
    name = models.CharField(max_length=30)
    # class_name = models.CharField(blank=True, max_length=2,choices=class_choice)
    class_name =  models.ForeignKey(classID,on_delete= models.CASCADE, default="", blank=True, null=True)
    roll_number = models.IntegerField(blank=True, null= True)
    enroll_by = models.ForeignKey(User,on_delete= models.CASCADE, default="", blank=True, null=True)


    class Meta:
        unique_together = ['class_name', 'roll_number']

    def __str__(self):
        str_name =  self.name  
        return str_name


class Attendance(models.Model):
    student_id = models.ForeignKey(Student,on_delete= models.CASCADE, default="")
    present = BooleanField()
    
    # date_present = models.DateTimeField(auto_now_add=True, blank=True)
    date_present = models.DateField(  blank=True,null=True)
    submit_date  = models.DateTimeField( auto_now_add=True, blank=True,null=True)
    teacher =  models.ForeignKey(User,on_delete= models.CASCADE, default="", blank=True, null=True)
    

class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete= models.CASCADE , blank=True, null=True)
    FirstName = models.CharField(max_length=50,blank=True, null=True)
    lastName = models.CharField(max_length=50,blank=True, null=True)
    gender = models.CharField(choices = [('Male','Male'),('Female','Female')] , max_length=10 , blank=True , null=True)
    birthday = models.DateField(blank=True, null = True)
    role = models.CharField(choices = [('Junior','Junior'),('Senior','Senior')] , max_length=10 , blank=True , null=True)
    subject = models.CharField(max_length=50,blank=True, null=True)
    dateOfJoining = models.DateField(blank=True, null = True)
    phone = models.CharField(max_length=10 , blank=True, null= True)
    email = models.EmailField(max_length=254, blank=True , null= True)
    profile_pic = models.ImageField( upload_to='attendance/profilePic', default = "{% static 'assets/img/profiles/avatar-02.jpg' %}" )
    # reportsTo = models.ForeignKey(User,on_delete= models.CASCADE, default="", blank=True, null=True)
    address = models.CharField(max_length=50,blank=True, null=True, default="")
    def __str__(self):
        str_name = f"{self.FirstName } {self.lastName}"
        # str_name =  self.FirstName 
        return str_name


class DayName(models.Model):
    dayNum = models.CharField( max_length=1,blank=True, null=True)
    dayName = models.CharField( max_length=10,blank=True, null=True)

    def __str__(self):
        return self.dayName


class TimeTable(models.Model):

    days = [
    ("0" ,"Monday"),
    ("1", 'Tuesday'),
    ("2","Wednessday"),
    ("3", "Thrusday"),
    ("4", "Friday"),
    ("5", "Saturday"),
    ("6", "Sunday"),
    ]




    periods=[
       ("1" ,"First"),
       ("2" ,"Second"),
       ("3" ,"Third"),
    ]

    # day = models.CharField( choices = days, max_length=20,blank=True, null=True)
    day =  models.ForeignKey(DayName,on_delete= models.CASCADE, default="", blank=True, null=True)
    period = models.CharField(choices = periods, max_length=20,blank=True, null=True)
    class_name =  models.ForeignKey(classID,on_delete= models.CASCADE, default="", blank=True, null=True)
    teacher =  models.ForeignKey(Profile,on_delete= models.CASCADE, default="", blank=True, null=True)
    

    def __str__(self):
        str_name =  self.class_name.className + " " +self.day.dayName +" " + self.period +"  "+ self.teacher.FirstName
        return str_name








# class Teacher(models.Model):
        
#     firstname = models.CharField(max_length=30,blank=True,default=" ")
#     lastname  =  models.CharField(max_length=30,blank= True, default=" ")
#     user      =  models.OneToOneField(User, on_delete=models.CASCADE)
    
#     # class_name = models.CharField(blank=True, max_length=2,choices=class_choice)
#     # class_name =  models.ForeignKey(classID,on_delete= models.CASCADE, default="", blank=True, null=True)
#     # roll_number = models.IntegerField(blank=True)
#     # enroll_teacher = models.ForeignKey(User,on_delete= models.CASCADE, default="", blank=True, null=True)

#     # class Meta:
#     #     unique_together = ['class_name', 'roll_number']

#     def __str__(self):
#         str_name =  self.firstname  
#         return str_name



# class ContactInfo(models.Model):
#     name=models.CharField(max_length=20)
#     email=models.EmailField(max_length=20)
#     address=models.TextField(max_length=20)

#     class Meta:
#         abstract=True

# class Customer(ContactInfo):
#     phone=models.IntegerField()

# class Staff(ContactInfo):
#     position=models.CharField(max_length=10)