from django.urls import path
from .api import *

urlpatterns = [
    path('job_field_parent/', get_job_field_parent),
    path('job_field/<int:id>/', get_job_field),
    path('create_projects/', create_projects),
]
