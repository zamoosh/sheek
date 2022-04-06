from django.urls import path
from .views import *

app_name = 'client'
urlpatterns = [
    path('auth/', auth, name="auth"),
    path('verify/', verify, name="verify"),
    path('logout/', Logout, name="logout"),
    path('dashboard/', dashboard, name="dashboard"),
    path('profile/', profile, name="profile"),
    path('expert-request/', expert_request, name="expert_request"),
    path('admins/', admins, name="admins"),
    path('experts/', experts, name="experts"),
    path('users/', users, name="users"),
    path('edit-admins/<int:id>/', edit_admins, name="edit_admins"),
    path('register-user/', register_user, name="register_user"),
]