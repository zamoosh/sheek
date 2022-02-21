from django.urls import path
from .views import *

app_name = 'client'
urlpatterns = [
    path('auth/', auth, name="auth"),
    path('verify/', verify, name="verify"),
    path('logout/', Logout, name="logout"),
    path('dashboard/', dashboard, name="dashboard"),
    path('profile/', profile, name="profile"),
    path('expert_request/', expert_request, name="expert_request"),
]