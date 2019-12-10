from django.db import models
from django.urls import reverse
from department.models import Department
from designation.models import Designation
from role.models import Role
from datetime import datetime
# Create your models here.


class EmployeeList(models.Model):
    name = models.CharField(max_length=150)
    salary = models.IntegerField(default=0)
    departments = models.ForeignKey(
        Department, on_delete=models.DO_NOTHING, default=1)
    phone = models.CharField(max_length=100, blank=None)
    email = models.CharField(max_length=100)
    photo = models.FileField(
        upload_to='documents/%Y/%m/%d/', default='documents/%Y/%m/%d/default.jpg')
    doj = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField()
    designations = models.ForeignKey(
        Designation, on_delete=models.DO_NOTHING, default=1, related_name="designations")
    roles = models.ForeignKey(
        Role, on_delete=models.DO_NOTHING, default=2)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.photo.delete()
        super().delete(*args, **kwargs)
