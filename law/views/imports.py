from django.shortcuts import render
from projects.models import *
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import jdatetime
from django.db.models import Q
import datetime
import time
from datetime import timedelta
from law.models import *