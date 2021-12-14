from django.urls import path
from .views import *

app_name = "state"
urlpatterns = [
    path('states/', state, name="state")
]