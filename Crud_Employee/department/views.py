from django.shortcuts import render, redirect, get_object_or_404
from .models import Department
from django.contrib import messages, auth
from department.forms import DepartmentForm
# Create your views here.


class DepartmentClass:
    def add_dept(request):
        if request.method == "POST":
            form = DepartmentForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('department_list')
        else:
            form = DepartmentForm()
        return form

    def department_list(request):
        department_list = Department.objects.order_by('-id')

        context = {
            'department_list': department_list
        }
        return context
