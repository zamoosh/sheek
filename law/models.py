from django.db import models


# Create your models here.

class Group(models.Model):
    title = models.CharField(max_length=250)


class Rule(models.Model):
    title = models.TextField(null=True, blank=True)
    date = models.CharField(max_length=25)
    article = models.TextField(null=True, blank=True)
    footnote = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)


