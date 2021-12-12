from django.urls import path
from .api import *
urlpatterns = [
    path('getme', api_get_me),
    path('login', login),
    path('user', user),
]
