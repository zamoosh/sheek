from django.db import models


# Create your models here.

class State(models.Model):
    status = models.BooleanField(default=True)
    title = models.CharField(max_length=50)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

