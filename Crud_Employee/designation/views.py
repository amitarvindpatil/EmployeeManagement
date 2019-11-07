from django.shortcuts import render, redirect, get_object_or_404
from .models import Designation
from django.contrib import messages, auth
from designation.forms import DesignationForm


# Create your views here.
class DesignationClass:
    # ----------------Retrive
    def designation_list():
        designation_list = Designation.objects.all()

        context = {
            'designation_list': designation_list
        }
        return context
# -----------Additon

    def add_designation(request):
        if request.method == "POST":
            form = DesignationForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('designation_list')
        else:
            form = DesignationForm()

        return form
# ----------------Update

    def edit_designation(request, id):
        edit_design = get_object_or_404(Designation, pk=id)
        context = {
            'edit_design': edit_design
        }
        return context

    def update_designation(request, id):
        if request.method == "POST":
            designation_data = Designation.objects.get(pk=id)
            designation_data.name = request.POST['name']
            designation_data.save()
            messages.success(request, "Data Deleted")
        return redirect("designation_list")

# --------------------Delete
    def del_designation(request, id):
        del_design = get_object_or_404(Designation, pk=id)
        context = {
            'del_design': del_design
        }
        return context

    def delete_designation(request, id):
        if request.method == "POST":
            delete_data = Designation.objects.get(pk=id)
            delete_data.delete()
            messages.error(request, "Data Deleted")
        return redirect('designation_list')
