from django.db import models


# Create your models here.

class Group(models.Model):
    title = models.CharField(max_length=250)


class Rule(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    date = models.DateField()
    article = models.CharField(max_length=250)
    footnote = models.TextField(null=True, blank=True)
    description = models.TextField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)


