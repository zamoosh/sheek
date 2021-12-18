from django.urls import path
from .api import *

urlpatterns = [
    path('expert/send_sms/', send_sms),
    path('expert/get_choice/', get_choice),
]
