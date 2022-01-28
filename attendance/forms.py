from django.forms import ModelForm, fields
from .models import Attendance, classID, Profile, User, Student

from django import forms
from django.contrib.auth.forms import UserCreationForm

class AttendanceForm(ModelForm):
    class Meta:
        model = Attendance
        fields = ['date_present']

class classForm(ModelForm):
    class Meta:
        model = classID
        fields = ['className']

class StudentRegisterForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'class_name']
 
class TeacherRegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','password']


class ProfileRegistrationForm(ModelForm):
    class Meta:
        model = Profile
        fields =['FirstName', 'lastName','role','subject']


class UpdateProfilePageForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['FirstName', 'lastName','user','role','subject']