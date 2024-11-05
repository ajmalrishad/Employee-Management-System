# Create your models here.
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=100)
    custom_fields = models.JSONField(default=dict, blank=True)  # For storing additional fields dynamically

    def __str__(self):
        return self.name
