from django.urls import path
from .views import *
from .apps import StateConfig

app_name = StateConfig.name
urlpatterns = [
    path('states/', state, name="state"),
    path('states/api/', state_api, name="stateapi"),
]
