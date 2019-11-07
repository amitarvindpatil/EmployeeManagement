from django.db import models

# Create your models here.


class Permissions(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        # return self.location
        return self.name
