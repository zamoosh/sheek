from django.urls import path
from .api import *

urlpatterns = [
    path('job_field_parent/', get_job_field_parent),
    path('get_masters_list/', get_masters_list),
    path('get_projects_list/', get_projects_list),
    path('get_job_field/', get_job_field),
    path('job_field/<int:id>/', get_job_field),
    path('get_one_project/<int:id>/', get_one_project),
    path('comment_rate/<int:id>/', comment_rate_projects),
    path('create_projects/', create_projects),
]
