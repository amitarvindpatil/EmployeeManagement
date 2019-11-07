from django.db import models
from permission.models import Permissions
# Create your models here.


class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        # return self.location
        return self.name


class Role_permissions(models.Model):
    roles = models.ForeignKey(
        Role, on_delete=models.DO_NOTHING)
    permissions = models.ForeignKey(Permissions, on_delete=models.DO_NOTHING)

    def __str__(self):
        # return self.location
        return self.id
