from django.db import models
from django.contrib.auth.models import AbstractUser
from unidecode import unidecode
from PIL import Image
from state.models import State
from library.ippanel import IpPanel


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
    existential = models.BooleanField(default=False)
    complete_pro = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if 'linkedin' not in self.extra:
            self.extra['linkedin'] = None
        if 'instagram' not in self.extra:
            self.extra['instagram'] = None
        if 'whatsapp' not in self.extra:
            self.extra['whatsapp'] = None
        if 'telegram' not in self.extra:
            self.extra['telegram'] = None

        if self.cellphone:
            self.cellphone = unidecode(self.cellphone)
        if self.cellphone is None:
            import re
            is_mobile_number = re.compile("^09?\d{9}$", re.IGNORECASE)
            if is_mobile_number.match(self.username):
                self.cellphone = self.username
        super(User, self).save()
        if self.image:
            try:
                img = Image.open(self.image)
                img.save(self.image.path, quality=95)
            except:
                pass

    def create_verificationcode(self):
        self.username = unidecode(self.username)
        VerificationCode.objects.filter(name=self.username).delete()
        vc = VerificationCode(name=self.username)
        vc.save()
        return str(vc.code)

    def get_verificationcode(self):
        VerificationCode.objects.filter(name=self.username, trying__gt=5).delete()
        try:
            vc = VerificationCode.objects.get(name=self.username)
            vc.trying += 1
            vc.save()
            return str(vc.code)
        except (VerificationCode.DoesNotExist, Exception):
            pass
        return None

    def sendsms(self):
        if not self.cellphone:
            return False
        code = self.create_verificationcode()
        try:
            values = {
                'verification-code': self.get_verificationcode(),
                'name': self.get_full_name() if self.first_name and self.last_name else self.cellphone
            }
            sms = IpPanel()
            sms.send_with_pattern(IpPanel.PATTERNS.get('enter_code'), self.cellphone, values)
        except (Exception, Exception):
            print('احتمالا اعتبار سامانه‌ی پیامکی تمام شده است!')
        print(code)


class VerificationCode(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.IntegerField()
    trying = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        import random
        if not self.code:
            self.code = random.randint(1000, 9999)
        super(VerificationCode, self).save()
