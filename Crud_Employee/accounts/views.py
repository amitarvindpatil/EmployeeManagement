from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages, auth
from emp_app.models import EmployeeList
from emp_app.models import Department
from designation.models import Designation


from django.core.files.storage import FileSystemStorage
from .forms import ImageUploadForm
from department.forms import DepartmentForm
from designation.forms import DesignationForm

from emp_app.forms import EmployeeForm
from designation.views import DesignationClass
from department.views import DepartmentClass
from emp_app.views import EmployeeClass
from role.views import RoleClass, RolePermissionsClass
from permission.views import PermissionClass
from hashlib import sha1
# Create your views here.


class Authentication:
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

                        employee_data = EmployeeList.objects.create(
                            name=first_name+last_name, email=email, user_id=user.id)

                        user.save()
                        employee_data.save()
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
            flag = True

            user = auth.authenticate(
                username=username, password=password)

            if user is not None:
                request.session['username'] = user.username

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
            try:
                del request.session['username']
                auth.logout(request)
            except KeyError:
                pass
            messages.success(request, 'You are logout Now')
            return redirect('index')

    def edit_changepassword(request, id):
        edit_password = get_object_or_404(User, pk=id)
        pass_context = {
            'edit_password': edit_password
        }
        return render(request, 'accounts/changepassword.html', pass_context)

    def changepassword(request, id):
        if request.method == "POST":
            oldpassword = request.POST['oldpassword']
            print(oldpassword)
            passwords = request.POST['password']
            # confirmpasswords = request.POST['confirmpassword']
            #     data = User.objects.filter(password=oldpassword)
            #     _, salt, hashpw = data.split('$')
            #     sha1(salt+data).hexdigest() == hashpw

            # print(data)
            # if data == True:
            #     messages.error(request, 'Pass')
            #     return redirect('dashboard')
            # else:
            #     messages.error(request, 'Complete Fail')
        return redirect('dashboard')


class Employees:

    def dashboard(request):
        context = EmployeeClass.dashboard(request)
        return render(request, 'accounts/emp_app/dashboard.html', context)

    # Add Record

    def add_record(request):
        add_context = EmployeeClass.add_record(request)
        return render(request, 'accounts/emp_app/add_employee.html', add_context)

    def create_employee(request):
        form = EmployeeClass.create_employee(request)
        return redirect('dashboard')

        # Modify Data
    def edit_info(request, id):
        edit_context = EmployeeClass.edit_info(request, id)
        return render(request, 'accounts/emp_app/edit_employee.html', edit_context)

    def edit_empuser(request, id):
        edit_empusercontext = EmployeeClass.edit_info(request, id)
        return render(request, 'accounts/emp_app/edit_empuser.html', edit_empusercontext)

    def update_data(request, id):
        form = EmployeeClass.update_data(request, id)
        return redirect('dashboard')

    def update_file(request, id):
        form = EmployeeClass.update_file(request, id)
        return redirect('dashboard')

        # Delete Data

    def del_info(request, id):
        del_context = EmployeeClass.del_info(request, id)
        return render(request, 'accounts/emp_app/del_employee.html', del_context)

    def del_data(request, id):
        form = EmployeeClass.del_data(request, id)
        return redirect('dashboard')

    def emp_search(request):
        emp_context = EmployeeClass.emp_search(request)
        return render(request, 'accounts/emp_app/emp_search.html', emp_context)

# -----------------------------Department Controlling------------------------------------------


class Departments:
    def add_dept(request):
        form = DepartmentClass.add_dept(request)
        return render(request, 'accounts/department/add_dept.html', {'form': form})

    def department_list(request):
        context = DepartmentClass.department_list(request)
        return render(request, 'accounts/department/department_list.html', context)


# -------------------------Designations Controlling-----------------------------------------

class Designations:
    def designation_list(request):
        context = DesignationClass.designation_list()
        return render(request, 'accounts/designation/designation_list.html', context)

    def add_designation(request):
        form = DesignationClass.add_designation(request)
        return render(request, 'accounts/designation/add_designation.html', {'form': form})

    def edit_designation(request, id):
        context = DesignationClass.edit_designation(request, id)

        return render(request, 'accounts/designation/edit_designation.html', context)

    def update_designation(request, id):
        form = DesignationClass.update_designation(request, id)
        return redirect("designation_list")

    def del_designation(request, id):
        context = DesignationClass.del_designation(request, id)

        return render(request, 'accounts/designation/del_designation.html', context)

    def delete_designation(request, id):
        form = DesignationClass.delete_designation(request, id)
        return redirect("designation_list")


# Pemission


def auth_permission_dash(request):

    return render(request, 'accounts/auth_and_permissions/auth_permission_dash.html')

# Roles Like admin and User


class Roles:
    def role_list(request):
        role_context = RoleClass.role_list(request)
        return render(request, 'accounts/auth_and_permissions/role/role_list.html', role_context)

# Permissions Like Insert/Update/Delete and Retrive


class RolePermissions:
    def role_permissions(request, id):
        rolepermission_context = RolePermissionsClass.role_permissions(
            request, id)
        return render(request, 'accounts/auth_and_permissions/role/role_permissions.html', rolepermission_context)

    def give_permissions(request, id):
        form = RolePermissionsClass.give_permissions(request, id)
        return redirect("role_list")

    def check_permissions(request):
        check_context = RolePermissionsClass.check_permissions(request)
        return render(request, 'accounts/auth_and_permissions/role/check_permissions.html', check_context)


class Permissions:
    def permission_list(request):
        permission_context = PermissionClass.permission_list(request)
        return render(request, 'accounts/auth_and_permissions/permissions/permission_list.html', permission_context)
