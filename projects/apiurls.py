from django.urls import path
from .api import *

urlpatterns = [
    path('job_field_parent/', get_job_field_parent),
    path('search/', search),
    path('get_masters_list/', get_masters_list),
    path('get_projects_list/', get_projects_list),
    path('get_job_field/', get_job_field),
    path('job_field/<int:id>/', get_job_field),
    path('get_job_field_field/<int:id>/', get_job_field_field),
    path('get_one_project/<int:id>/', get_one_project),
    path('comment_rate/<int:id>/', comment_rate_projects),
    path('send_message/<int:id>/', send_message),
    path('get_message/<int:id>/', get_message),
    path('get_jobfield_bytag/<int:id>/', get_jobfield_bytag),
    path('create_projects/', create_projects),
    path('create_complaint/', create_complaint),
    path('get_complaint_list/', get_complaint_list),
    path('create_text/', create_text),
    path('get_complaint_done/<int:id>/', get_complaint_done),
    path('get_complaint_one/<int:id>/', get_complaint_one),
    path('set_user_jobfied/', set_user_jobfied),
    path('set_state_expert/<int:jobfield>/', set_state_expert),
    path('get_state/<int:jobfield>/', get_state),
]
