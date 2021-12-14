from django.urls import path
from .views import *
from .apps import ProjectsConfig

app_name = ProjectsConfig.name
urlpatterns = [
    path('jobs/', jobs, name="jobs"),
    path('jobs/api/', jobs_api, name="jobsapi"),
]
