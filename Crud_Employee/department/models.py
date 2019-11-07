from django.db import models

# Create your models here.


class Department(models.Model):
    deptname = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        # return self.location
        return "(%s) %s" % (self.deptname, self.location)
