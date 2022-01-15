from django.urls import path
from .views import *
from .apps import StateConfig

app_name = StateConfig.name
urlpatterns = [
    path('states/', state, name="state"),
    path('state/delete/<int:id>', delete_state, name="deletestate"),
    path('states/api/', state_api, name="stateapi"),
    path('states/api/<int:parent>/', state_api, name="stateapi"),
]
