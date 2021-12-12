from django.db import models
from projects.models import UserJobField, Project

# Create your models here.

from django.db import models
from uuid import uuid4
from django.contrib.auth import get_user_model
from PIL import Image
import os
from django.conf import settings
from minio import Minio
from datetime import timedelta

User = get_user_model()


class File(models.Model):
    name = models.CharField(max_length=400, unique=True)
    description = models.TextField(null=True, blank=True)
    key = models.CharField(max_length=200, unique=True, blank=True)
    extra = models.JSONField(default=dict)
    buket = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_jobField = models.ForeignKey(UserJobField, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        client = Minio(settings.MINIO_CLIENT,
                       access_key=settings.MINIO_ACCESS_KEY,
                       secret_key=settings.MINIO_SECRET_KEY, secure=True)
        found = client.bucket_exists(settings.MINIO_BUKET)

        if not found:
            client.make_bucket(settings.MINIO_BUKET)

        if 'status' not in self.extra:
            self.extra['status'] = False
        if self.buket == '':
            self.buket = settings.MINIO_BUKET
        if self.key == '':
            key = str(uuid4())
            while File.objects.filter(key=key).exists():
                key = str(uuid4())
            self.key = key
        if self.name == '':
            self.name = self.extra['name']
            while File.objects.filter(models.Q(name=self.name) & ~models.Q(id=self.id)).exists():
                self.name = self.create_name()
        if self.extra['status']:
            self.update_info()
        super(File, self).save()


    def moved(self):
        if 'move' not in self.extra:
            file_old_path = os.path.join(settings.MEDIA_ROOT, 'tmp', str(self.owner.id), self.name)
            if not os.path.exists(os.path.join(settings.MEDIA_ROOT, self.extra['module'], str(self.extra['id']))):
                os.makedirs(os.path.join(settings.MEDIA_ROOT, self.extra['module'], str(self.extra['id'])))
            os.rename(file_old_path,
                      os.path.join(settings.MEDIA_ROOT, self.extra['module'], str(self.extra['id']), self.name))
            self.extra['move'] = True
            self.name = os.path.join(self.extra['module'], str(self.extra['id']), self.name)
            super(File, self).save()


    def get_file_path(self):
        if 'move' in self.extra:
            return os.path.join(settings.MEDIA_ROOT, self.extra['module'], str(self.extra['id']), self.name)


    def update_info(self):
        return True


    def create_name(self):
        return '.'.join(self.extra['name'].split(".")[:-1]) + str(uuid4()) + "." + self.extra['name'].split(".")[-1]


    def get_url(self, hours=2):
        client = Minio(settings.MINIO_CLIENT,
                       access_key=settings.MINIO_ACCESS_KEY,
                       secret_key=settings.MINIO_SECRET_KEY, secure=True)
        url = client.get_presigned_url("GET", settings.MINIO_BUKET, self.name, expires=timedelta(hours=hours))
        return url
