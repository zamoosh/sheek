from django.urls import path
from .api import *

urlpatterns = [
    path('expert/get_expert/', get_expert),
]
