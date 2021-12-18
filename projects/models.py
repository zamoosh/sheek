from django.db import models
from django.contrib.auth import get_user_model
from state.models import State

User = get_user_model()


class JobField(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    description = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)


class UserJobField(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField()
    status = models.BooleanField(default=True)
    delete = models.BooleanField(default=False)
    status_comment = models.CharField(max_length=250)
    experience = models.DateTimeField()
    jobField = models.ForeignKey(JobField, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)


class Project(models.Model):
    rate = models.IntegerField()
    status = models.BooleanField(default=True)
    TYPE = (
        (0, 'before confirm'),
        (1, 'progress'),
        (2, 'done'),
    )
    status_jobField_user = models.IntegerField(choices=TYPE, default=1)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    user_jobField = models.ForeignKey(UserJobField, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)


class Message(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    user_view = models.BooleanField(default=False)
    expert_view = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
