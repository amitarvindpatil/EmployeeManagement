from django.contrib import admin
from .models import EmployeeList
# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'salary',
                    'phone', 'email', 'photo', 'departments', 'doj')


admin.site.register(EmployeeList, EmployeeAdmin)
