from django.urls import path
from .views import *

app_name = 'law'
urlpatterns = [
    path('law/<int:id>/', laws, name="laws"),
]