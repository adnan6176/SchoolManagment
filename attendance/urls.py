from django.contrib import admin
from django.urls import path , include
from  . import views

urlpatterns = [
    path('', views.loginuser1, name='login1'),
    path('signup/', views.signupuser, name='signupuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('dashboard/<str:class_id>', views.dashboard, name='dashboard'),
    path('attendance/<str:class_id>', views.attendance, name='attendance'),
    path('viewAttendance/', views.viewAttendance, name='viewAttendance'),
    path('currentPage/', views.currentPage, name='currentPage'),
    path('makeAttendance/', views.makeAttendance, name='makeAttendance'),
    path('newpage/', views.newpage, name='newpage'),
    path('teacherProfilePage/', views.teacherProfilePage, name='teacherProfilePage'),
    path('profilepage/<str:id>', views.profilepage, name='profilepage'),
    path('blankPage/', views.blankPage, name='blankPage'),
    path('redirectDashboard/', views.redirectDashboard, name='redirectDashboard'),
    path('employeeDashboard/<str:id>', views.employeeDashboard, name = 'employeeDashboard'),
    path('login1/', views.loginuser1, name='loginuser1'),
    path('forgetpassword/', views.forgetpassword, name='forgetpassword'),
    path('signup/', views.signupuser, name='signupuser'),
    path('register/', views.register, name='register'),
    path('signoutuser/', views.signoutuser, name='signoutuser'),
    path('signoutuser/', views.signoutuser, name='signoutuser'),
    path('viewAttendances/', views.viewAttendances, name='viewAttendances'),
    path('makeAttendances/', views.makeAttendances, name='makeAttendances'),
    path('assignClassFormTeacher/', views.assignClassFormTeacher, name='assignClassFormTeacher'),
    path('editTeacherTimeTable/', views.editTeacherTimeTable, name='viewTeacherTimeTable'),
    path('addStudentForm/', views.addStudentForm, name='addStudentForm'),
    path('addTeacherForm/', views.addTeacherForm, name='addTeacherForm'),
    path('addTeacherPage', views.editProfilePage, name='editProfilePage'),
    
]