from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def dashboard(request):
  return render(request,'dashboard.html')


# Function for displaying Employees
def display_employee(request):
  items = Employee.objects.all()
  return render(request, 'dashboard.html', {'items': items})

# Function for addinf the employee
def add_employee(request):
  if request.method == "POST":
        form=EmployeeForm(request.POST)
        if form.is_valid():
          form.save()
          return redirect('display_employee')
  else:
      form = EmployeeForm()
      return render(request,'add_employee.html',{'from':form})


# Function for editing the employees
def edit_employee(request):
  items = get_object_or_404(Employee)
  
  if request.method =="POST":
    form=EmployeeForm(request.POST, instance = item)
    if form.is_valid():
          form.save()
          return redirect('display_employee')

    else:
      
      form = EmployeeForm(instance = form)
      return render(request, 'edit.html', {'form':form})


#Function to delete employe
def delete_employee(request,pk):
  Employee.objects.filter(id=pk).delete()
  
  items = Employee.objects.all()
  return render(request, 'dashboard.html', {'items': items})