from django.db import models
from django.contrib.auth.models import AbstractUser
from unidecode import unidecode
from PIL import Image
from state.models import State


def user_image(instance, filename):
    return "%s/%s/%s" % ('profile', instance.id, filename)


def national_card_image(instance, filename):
    return "%s/%s/%s" % ('national_card', instance.id, filename)


class User(AbstractUser):
    national_card = models.ImageField(blank=True, null=True, upload_to=national_card_image)
    cellphone = models.CharField(max_length=15, unique=True, blank=True, null=True)
    national_code = models.CharField(max_length=10, blank=True, null=True, unique=True)
    birthday = models.DateField(null=True, blank=True)
    extra = models.JSONField(default=dict)
    image = models.ImageField(blank=True, null=True, upload_to=user_image)
    gender = models.BooleanField(default=True)
    has_jobField = models.BooleanField(default=False)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True, blank=True)
    social = models.CharField(max_length=250)

    def save(self, *args, **kwargs):
        if self.cellphone:
            self.cellphone = unidecode(self.cellphone)
        if self.cellphone is None:
            import re
            is_mobile_number = re.compile("^09?\d{9}$", re.IGNORECASE)
            if is_mobile_number.match(self.username):
                self.cellphone = self.username
        super(User, self).save()
        if self.image:
            img = Image.open(self.image)
            img.save(self.image.path, quality=95)


class VerificationCode(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.IntegerField()
    trying = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.name = unidecode(self.name)
        super(VerificationCode, self).save()
