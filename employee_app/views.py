from multiprocessing import context
from urllib import request
from django.shortcuts import render,HttpResponse
from .models import Role,Department,Employee
from datetime import datetime
from django.db.models import Q

# Create your views here.
def index(req):
    return render(req,'index.html')

def all_emp(req):
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    print(context)
    return render(req,'viewall_emp.html',context)

def add_emp(req):
    if req.method =='POST':
        first_name=req.POST.get('first_name')
        last_name=req.POST.get('last_name')
        salary=int(req.POST.get('salary'))
        bonus=int(req.POST.get('bonus'))
        phone=int(req.POST.get('phone'))
        dept=int(req.POST.get('dept'))
        role=int(req.POST.get('role'))
        new_emp=Employee(first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,phone=phone,dept_id=dept,role_id=role,hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("Employee added successfully!!!")
    elif req.method=="GET":
        return render(req,'add_emp.html')
        
    else:
        return HttpResponse("an error has occured")

    return render(req,'add_emp.html')

def remove_emp(req,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed=Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee successfully removed ")
        except:
            return HttpResponse("Please enter a valid employee ID")

    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    print(context)
    return render(req,'remove_emp.html',context)

def filter_emp(req):
    if req.method=='POST':
        name=req.POST.get('name')
        dept=req.POST.get('dept')
        role=req.POST.get('role')
        emps=Employee.objects.all()
        if name:
            emps=emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emps=emps.filter(dept__name=dept)
        if role:
            emps=emps.filter(role__name=role)
        context={'emps':emps}
        return render(req,'viewall_emp.html',context)
    elif req.method=='GET':
        return render(req,'filter_emp.html')
    else:
        return HttpResponse("there is an error filtering in employees")

