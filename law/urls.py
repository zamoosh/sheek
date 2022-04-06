from django.urls import path
from .views import *

app_name = 'law'
urlpatterns = [
    path('laws/', laws, name="laws"),
    path('law/<int:id>/', law, name="law"),
]