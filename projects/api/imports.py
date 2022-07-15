from django.core.mail import send_mail
from django.db.models import Q, Sum, Count, QuerySet
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.shortcuts import render
import re
from django.core.validators import validate_email
from django import forms
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.conf import settings
from django.http.response import HttpResponseRedirect
import datetime

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.status import *

from ..dto import *
from client.dto import UserViewDto
from client.models import *
from client.serializer import UserSerializer
import numpy as np


def send_mail_func(message, email_address):
    status = send_mail(
        "درخواست فعال سازی حساب کاربری {title}".format(title="ویدان"),
        str(message),
        'app@vidone.org',
        [email_address],
        # fail_silently=False,
    )
    print(status)
