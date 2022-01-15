from django.http import JsonResponse
from django.shortcuts import render
from state.models import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required