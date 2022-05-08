from django.urls import path
from .views import *

app_name = 'log'
urlpatterns = [
    path('reports/', reports, name="reports")
]