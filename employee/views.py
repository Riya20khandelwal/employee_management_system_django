from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, logout, authenticate
# Create your views here.

def index(request):
    return render(request, 'index.html')


def registration(request):
    error = ""
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['empcode']
        em = request.POST['email']
        pwd = request.POST['pwd']

        try:
            user = User.objects.create_user(first_name=fn, last_name=ln, username=em, password=pwd)
            EmployeeDetail.objects.create(user=user, empcode=ec)
            EmployeeExperience.objects.create(user=user)
            EmployeeEducation.objects.create(user=user)
            
            error = "no"

        except:
            error = "yes"

    return render(request, 'registration.html', locals())


def emp_login(request):
    error = ""
    if request.method =="POST":
        u = request.POST['emailid']
        p = request.POST['password']

        user = authenticate(username=u, password=p)

        if user:
            login(request, user)
            error = 'no'
        else:
            error = 'yes'

    return render(request, 'emp_login.html', locals())


def emp_home(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    return render(request, 'emp_home.html')

def profile(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    user = request.user
    employee = EmployeeDetail.objects.get(user=user)
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['empcode']
        dept = request.POST['department']
        designation = request.POST['designation']
        contact = request.POST['contact']
        jdate = request.POST['jdate']
        gender = request.POST['gender']

        employee.user.first_name = fn
        employee.user.last_name = ln
        employee.empcode = ec
        employee.empdept = dept
        employee.designation = designation
        employee.contact = contact
        employee.gender = gender

        if jdate:
            employee.joiningdate = jdate

        try:
            employee.save()
            employee.user.save()
            error = "no"

        except:
            error = "yes"

    return render(request, 'profile.html', locals())

def Logout(request):
    logout(request)
    return redirect('index')

def my_experience(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')

    user = request.user
    experience = EmployeeExperience.objects.get(user=user)


    
    return render(request, 'myexperience.html', locals())


def edit_myexperience(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    user = request.user
    experience = EmployeeExperience.objects.get(user=user)
    if request.method == "POST":
        fcn = request.POST['company1name']
        fcd = request.POST['company1desig']
        fcs = request.POST['company1salary']
        fcdu = request.POST['company1duration']
        
        scn = request.POST['company2name']
        scd = request.POST['company2desig']
        scs = request.POST['company2salary']
        scdu = request.POST['company2duration']

        tcn = request.POST['company3name']
        tcd = request.POST['company3desig']
        tcs = request.POST['company3salary']
        tcdu = request.POST['company3duration']

        experience.company1name = fcn
        experience.company1desig = fcd
        experience.company1salary = fcs
        experience.company1duration = fcdu
        
        experience.company2name = scn
        experience.company2desig = scd
        experience.company2salary = scs
        experience.company2duration = scdu

        experience.company3name = tcn
        experience.company3desig = tcd
        experience.company3salary = tcs
        experience.company3duration = tcdu


        try:
            experience.save()
            error = "no"

        except:
            error = "yes"

    return render(request, 'edit_myexperience.html', locals())


def my_education(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')

    user = request.user
    education = EmployeeEducation.objects.get(user=user)


    
    return render(request, 'my_education.html', locals())


def edit_myeducation(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    user = request.user
    education = EmployeeEducation.objects.get(user=user)
    if request.method == "POST":
        coursepg = request.POST['coursepg']
        schoolclgpg = request.POST['schoolclgpg']
        yearofpassingpg = request.POST['yearofpassingpg']
        percentagepg = request.POST['percentagepg']
        
        coursegra = request.POST['coursegra']
        schoolclggra = request.POST['schoolclggra']
        yearofpassinggra = request.POST['yearofpassinggra']
        percentagegra = request.POST['percentagegra']

        coursessc = request.POST['coursessc']
        schoolclgssc = request.POST['schoolclgssc']
        yearofpassingssc = request.POST['yearofpassingssc']
        percentagessc = request.POST['percentagessc']

        coursehsc = request.POST['coursehsc']
        schoolclghsc = request.POST['schoolclghsc']
        yearofpassinghsc = request.POST['yearofpassinghsc']
        percentagehsc = request.POST['percentagehsc']
        

        education.coursepg = coursepg
        education.schoolclgpg = schoolclgpg
        education.yearofpassingpg = yearofpassingpg
        education.percentagepg = percentagepg
        
        education.coursegra = coursegra
        education.schoolclggra = schoolclggra
        education.yearofpassinggra = yearofpassinggra
        education.percentagegra = percentagegra

        education.coursessc = coursessc
        education.schoolclgssc = schoolclgssc
        education.yearofpassingssc = yearofpassingssc
        education.percentagessc = percentagessc
        
        education.coursehsc = coursehsc
        education.schoolclghsc = schoolclghsc
        education.yearofpassinghsc = yearofpassinghsc
        education.percentagehsc = percentagehsc

        try:
            education.save()
            error = "no"

        except:
            error = "yes"

    return render(request, 'edit_myeducation.html', locals())

def change_password(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    user = request.user

    if request.method == "POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']

        try:
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error = "no"
            else:
                error = "not"

        except:
            error = "yes"

    return render(request, 'change_password.html', locals())


def admin_login(request):
    error = ""
    if request.method =="POST":
        u = request.POST['username']
        p = request.POST['pwd']

        user = authenticate(username=u, password=p)
        
        try:
            if user.is_staff:
                login(request, user)
                error = 'no'
            else:
                error = 'yes'
        except:
            error = "yes"

    return render(request, 'admin_login.html', locals())

def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request, 'admin_home.html')

def change_passwordadmin(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    user = request.user

    if request.method == "POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']

        try:
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error = "no"
            else:
                error = "not"

        except:
            error = "yes"

    return render(request, 'change_passwordadmin.html', locals())