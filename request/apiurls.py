from django.urls import path
from .api import *

urlpatterns = [
    path('expert/random/', get_choice),
]
