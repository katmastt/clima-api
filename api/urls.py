from django.contrib import admin
from django.urls import path
from clima_api.views import remaining_jobs
#from django.conf.urls import url
from django.urls import include, re_path

urlpatterns = [
    path(r'project_id/<id>', remaining_jobs, name='context_name-details'),
    
]