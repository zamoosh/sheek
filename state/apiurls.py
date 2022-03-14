from django.urls import path
from .api import *

urlpatterns = [
    path('province/', get_province),
    path('city/<int:city>/', get_city),
]
