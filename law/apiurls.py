from django.urls import path
from .api import *

urlpatterns = [
    path('get_category/', get_category),
    path('get_category/<int:pk>/', get_rule),
]
