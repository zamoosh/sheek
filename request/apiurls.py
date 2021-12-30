from django.urls import path
from .api import *

urlpatterns = [
    path('expert/get_choice/', get_choice),
]
