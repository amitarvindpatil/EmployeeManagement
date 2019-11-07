from django import forms
from .models import EmployeeList


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeList
        fields = ('name', 'salary', 'departments',
                  'phone', 'email', 'photo', 'user_id')

    def __str__(self):
        return self.name
