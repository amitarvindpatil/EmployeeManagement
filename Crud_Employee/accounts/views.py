from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages, auth
from emp_app.models import EmployeeList
from django.core.files.storage import FileSystemStorage
from .forms import ImageUploadForm
# Create your views here.


def registration(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

# Password Confirmation
        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username already Taken')
                return redirect('registration')
            else:
                # Email Id Confirmation
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email already Taken')
                    return redirect('registration')
                else:
                    user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                                    email=email, password=password)
                    user.save()
                    messages.success(
                        request, 'You are now registerd and can log in')
                    return redirect('login')
        else:
            messages.error(request, 'Password Not Match')
            return redirect('registration')
    else:
        return render(request, 'accounts/registration.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(
            username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are now logged in")
            return redirect('dashboard')
        else:
            messages.error(request, "invalid Credentials")
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are logout Now')
        return redirect('index')


def dashboard(request):
    dashboard_list = EmployeeList.objects.order_by('-id')

    context = {
        'dashboard_list': dashboard_list
    }
    return render(request, 'accounts/dashboard.html', context)

# Add Record


def add_record(request):
    return render(request, 'accounts/add_employee.html')


def create_employee(request):

    if request.method == "POST":

        name = request.POST['name']
        salary = request.POST['salary']
        department = request.POST['department']
        phone = request.POST['phone']
        email = request.POST['email']
        photo = request.FILES['photo']
        employee_data = EmployeeList.objects.create(
            name=name, salary=salary, department=department, phone=phone, email=email, photo=photo)
        employee_data.save()
        messages.success(request, "Data Added successfully")

    return redirect('dashboard')


# Modify Data

def edit_info(request, id):
    edit_data = get_object_or_404(EmployeeList, pk=id)
    context = {
        'edit_data': edit_data
    }
    return render(request, 'accounts/edit_employee.html', context)


def update_data(request, id):
    if request.method == "POST":
        empdata = EmployeeList.objects.get(pk=id)
        empdata.name = request.POST['name']
        empdata.salary = request.POST['salary']
        empdata.department = request.POST['department']
        empdata.phone = request.POST['phone']
        empdata.email = request.POST['email']

        empdata.save()
        messages.success(request, "Data Updated")
    return redirect('dashboard')


def update_file(request, id):
    if request.method == "POST":
        empimage = EmployeeList.objects.get(pk=id)

        empimage.photo = request.FILES['photo']
        empimage.save()
        messages.success(request, "Image Updated")
    return redirect('dashboard')

    # Delete Data


def del_info(request, id):
    del_data = get_object_or_404(EmployeeList, pk=id)
    context = {
        'del_data': del_data
    }
    return render(request, 'accounts/del_employee.html', context)


def del_data(request, id):
    if request.method == "POST":
        delete_data = EmployeeList.objects.get(pk=id)
        delete_data.delete()
        messages.error(request, "Data Deleted")
    return redirect('dashboard')
