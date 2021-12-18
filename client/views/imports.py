from django.http.response import HttpResponseRedirect
import datetime
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
User = get_user_model()
from state.models import State
import re
from library.smsir import Smsir
