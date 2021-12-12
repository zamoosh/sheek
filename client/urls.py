from django.urls import path
from .views import *

app_name = 'client'
urlpatterns = [
    path('singing/', singing, name="singing"),
    path('verify/', verify, name="verify"),
    path('logout/', Logout, name="logout"),
    path('dashboard/', dashboard, name="dashboard"),
    path('profile/', profile, name="profile"),
]