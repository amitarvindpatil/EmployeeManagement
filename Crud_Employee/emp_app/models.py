from django.db import models
from django.urls import reverse
# Create your models here.


class EmployeeList(models.Model):
    name = models.CharField(max_length=150)
    salary = models.IntegerField()
    department = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    photo = models.FileField(
        upload_to='documents/%Y/%m/%d/')

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.photo.delete()
        super().delete(*args, **kwargs)
