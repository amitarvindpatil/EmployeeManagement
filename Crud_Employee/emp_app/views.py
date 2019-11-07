from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from .models import EmployeeList
import json
from django.core.serializers import serialize
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
# For Pagination
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from emp_app.models import Department, Designation, Role

# --------------------Employee FrontEnd


class EmployeeFrontView:

    def listings(request):
        employee_list = EmployeeList.objects.order_by('-id')
        paginator = Paginator(employee_list, 5)
        page = request.GET.get('page')
        page_listings = paginator.get_page(page)
        context = {
            'employee_list': page_listings
        }
        return render(request, 'listings/listings.html', context)

    def listingsjson(request):
        employee_json = EmployeeList.objects.all().values()
        context = list(employee_json)
        return JsonResponse(context, safe=False)

    def employee_details(request, id):
        employee_detail = get_object_or_404(EmployeeList, pk=id)
        context = {
            'employee_detail': employee_detail
        }
        return render(request, 'listings/employee_details.html', context)

    # Search

    def search(request):
        search_data = EmployeeList.objects.order_by("-id")

        if 'name' in request.GET:
            name = request.GET['name']
            if name:
                search_data = search_data.filter(name__icontains=name)
        context = {
            'search_data': search_data,
        }
        print(context)
        return render(request, 'listings/search.html', context)


# --------------------Employee Backend----------------------
class EmployeeClass:
    def dashboard(request):

        dashboard_list = EmployeeList.objects.order_by(
            '-id').filter(user_id=request.user.id)

        paginator = Paginator(dashboard_list, 6)
        page = request.GET.get('page')
        page_listings = paginator.get_page(page)

        context = {
            'dashboard_list': page_listings
        }
        return context

    def departmentdata():
        depts = Department.objects.all()
        dept_context = {
            'depts': depts
        }
        return dept_context

    def designationdata():
        desg = Designation.objects.order_by('id')
        desg_context = {
            'desg': desg
        }
        return desg_context

    def roledata():
        role = Role.objects.order_by('id')
        role_context = {
            'role': role
        }
        return role_context

    def add_record(request):
        employee_list = EmployeeList.objects.filter(roles_id=2)
        paginator = Paginator(employee_list, 5)
        page = request.GET.get('page')
        page_listings = paginator.get_page(page)
        add_context = {
            'employee_list': page_listings
        }

        return add_context

    def emp_search(request):
        search_data = EmployeeList.objects.order_by("-id")

        if 'name' in request.GET:
            name = request.GET['name']
            if name:
                search_data = search_data.filter(name__icontains=name)
        emp_context = {
            'search_data': search_data
        }
        return emp_context

    def edit_info(request, id):
        edit_data = get_object_or_404(EmployeeList, pk=id)

        add_context_dept = EmployeeClass.departmentdata()
        add_context_desg = EmployeeClass.designationdata()
        add_context_role = EmployeeClass.roledata()

        context_emp = {
            'edit_data': edit_data
        }

        def mergedata(context_emp, add_context_dept, add_context_desg, add_context_role):
            mgdata = {**context_emp, **add_context_dept, **
                      add_context_desg, **add_context_role}
            return mgdata
        edit_context = mergedata(context_emp,
                                 add_context_dept, add_context_desg, add_context_role)

        return edit_context

    def update_data(request, id):
        if request.method == "POST":
            empdata = EmployeeList.objects.get(pk=id)
            empdata.name = request.POST['name']
            empdata.salary = request.POST['salary']
            print(request.POST['salary'])
            empdata.departments_id = request.POST['departments']
            empdata.designations_id = request.POST['designations']
            empdata.roles_id = request.POST['roles']

            empdata.phone = request.POST['phone']
            empdata.email = request.POST['email']

            empdata.save()
            messages.success(request, "Data Updated")
        return redirect('add_record')

    def update_file(request, id):
        if request.method == "POST":
            empimage = EmployeeList.objects.get(pk=id)

            empimage.photo = request.FILES['photo']
            empimage.save()
            messages.success(request, "Image Updated")
        return redirect('dashboard')

    def del_info(request, id):
        del_data = get_object_or_404(EmployeeList, pk=id)

        del_context = {
            'del_data': del_data
        }
        return del_context

    def del_data(request, id):
        if request.method == "POST":
            delete_data = EmployeeList.objects.get(pk=id)
            delete_data.delete()
            messages.error(request, "Data Deleted")
        return redirect('dashboard')
