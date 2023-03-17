from django.urls import path
from app2.views import *

app_name='nothing'

urlpatterns=[
    path('sahana/',sahana,name='sahana'),
]