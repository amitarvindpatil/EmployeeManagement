from django import forms
from .models import Designation


class DesignationForm(forms.ModelForm):
    class Meta:
        model = Designation
        fields = "__all__"
