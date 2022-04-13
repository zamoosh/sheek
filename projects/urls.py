from django.urls import path
from .views import *
from .apps import ProjectsConfig

urlpatterns = [
    path('jobs/', jobs, name="jobs"),
    path('jobs/delete/<int:id>/', delete_job, name="delete-job"),
    path('jobs/api/', jobs_api, name="jobsapi"),
    path('jobs-competence/api/', jobs_competence_api, name="jobs_competence_api"),
    path('job-group-api/api/', jobs_group_api, name="jobs_group_api"),
    path('job-group-api/api/<int:parent>/', jobs_group_api, name="jobs_group_api"),
    path('user-job/', userjobfield, name="userjob"),

    path('user-state/', userstate, name="userstate"),
    path('add-userstate/<int:id>/', adduserstate, name="adduserstate"),
    path('add-userstateapi/<int:id>/', userstateapi, name="userstateapi"),
    path('dell-userstateapi/<int:id>/', dellstate, name="dellstate"),
    path('get_userstateapi/<int:id>/', get_userstateapi, name="get_userstateapi"),

    path('new-adduserjob/', adduserjobfield, name="adduserjob"),
    path('new-adduserjob/<int:id>/', adduserjobfields, name="adduser-jobs"),
    # path('adduserjob/<int:parent>/', jobs_api, name="adduserjobhh"),

    # path('adduser-parent-api/', adduser_parent_api, name="adduser_parent_api"),
    # path('adduser-parent-api/<int:parent>/', adduser_parent_api, name="adduser_parent_api"),

    path('adduser-job-api/', adduser_jobs_api, name="adduser-job-api"),
    path('adduser-job-api/<int:id>/', adduser_jobs_api, name="adduser-job-api"),

    path('adduserjob/api/', jobs_api_search, name="jobs_api_search"),
    path('adduserjob/api/<int:parent>/', jobs_api_search, name="jobs_api_search"),

    path('adduserjob/api2/', jobs_api_search2, name="jobs_api_search2"),
    path('adduserjob/api2/<int:parent>/', jobs_api_search2, name="jobs_api_search2"),

    path('addproject/', addproject, name="addproject"),
    path('addproject-api/', userjob_api, name="addproject_api"),
    path('project-done/', redierct, name="redierct"),
    path('projects/', get_projects, name="projects"),
    path('expert-projects/', get_expert_projects, name="expert-projects"),
    path('project/<int:id>/reject/', reject_project, name="reject_project"),
    path('project/<int:id>/end/', end_project, name="end_project"),
    path('project-request/', project_request, name="project-request"),
    path('project/<int:id>/', view_project, name="view_project"),
    path('report/api/<int:id>/', report_api, name="getReport"),
    path('message/api/<int:id>/', message_api, name="getMessage"),
    path('message/readmsg/<int:id>/', setreadmessage, name="ReadMessage"),
    path('experts/', experts, name="experts"),
    path('jobsearch/api/', job_search, name="job_search"),

    path('admin_complaints/', admin_complaints, name="admin_complaints"),
    path('complaints/', complaints, name="complaints"),
    path('new-complaint/', add_complaint, name="add_complaint"),
    path('complaint/<int:id>/<str:title>/', view_complaint, name="view_complaint"),
    path('end_complaint/<int:id>/', end_complaint, name="end_complaint"),
    path('projects/api/', projects_api, name="project_api"),
]

app_name = ProjectsConfig.name
app_name = ProjectsConfig.name
