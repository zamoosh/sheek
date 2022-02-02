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

    def delete(self, *args, **kwargs):
        self.status = False
        self.save()


class Tag(models.Model):
    title = models.CharField(max_length=250, unique=True)
    jobfield = models.ForeignKey(JobField, on_delete=models.CASCADE)


class UserJobField(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    delete = models.BooleanField(default=False)
    status_comment = models.CharField(max_length=250)
    experience = models.DateField()
    jobField = models.ForeignKey(JobField, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    description = models.TextField()


class Project(models.Model):
    title = models.CharField(max_length=250)
    rate = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    TYPE = (
        (0, 'before confirm'),
        (1, 'progress'),
        (2, 'done'),
    )
    status_jobField_user = models.IntegerField(choices=TYPE, default=0)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    jobField = models.ForeignKey(JobField, on_delete=models.CASCADE, null=True, blank=True)
    user_jobField = models.ForeignKey(UserJobField, on_delete=models.CASCADE, null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    update_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    user_view = models.BooleanField(default=False)
    expert_view = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Report(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=250)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.TextField()
    projects = models.ForeignKey(Project, on_delete=models.CASCADE)
