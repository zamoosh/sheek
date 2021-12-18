from django.urls import path
from .views import *
from .apps import ProjectsConfig

app_name = ProjectsConfig.name
urlpatterns = [
    path('jobs/', jobs, name="jobs"),
    path('jobs/delete/<int:id>', delete_job, name="delete-job"),
    path('jobs/api/', jobs_api, name="jobsapi"),
    path('user-job/', userjobfield, name="userjob"),
]
