from django.urls import path
from .api import *

urlpatterns = [
    path('expert/get_expert/', get_expert),
    path('expert/get_user/', get_user),
    path('expert/get_expert_one/<int:id>/', get_expert_one),
]
