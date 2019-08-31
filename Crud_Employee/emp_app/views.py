from django.shortcuts import render, redirect, get_object_or_404
from .models import EmployeeList
import json
from django.core.serializers import serialize
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
# For Pagination
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def listings(request):
    employee_list = EmployeeList.objects.order_by('-id')
    paginator = Paginator(employee_list, 2)
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)
    context = {
        'employee_list': page_listings
    }
    return render(request, 'listings/listings.html', context)


def listingsjson(request):
    employee_json = EmployeeList.objects.all()
    json_list = []
    for jsl in employee_json.values():
        json_list.append(jsl)
        # print(temp_list)
    context = {
        'employee_json': json_list
    }

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
