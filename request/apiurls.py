from django.urls import path
from .api import *

urlpatterns = [
    path('expert/get_expert/', get_expert),
    path('expert/get_user/', get_user),
    path('expert/get_project_for_expert/', get_project_for_expert),
    path('expert/get_expert_one/<int:id>/', get_expert_one),
    path('expert/confirm_project/<int:id>/', confirm_project),
    path('expert/get_jobfield_for_expert/', get_jobfield_for_expert),
]
