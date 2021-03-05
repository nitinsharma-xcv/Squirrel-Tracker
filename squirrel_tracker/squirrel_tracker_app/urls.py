# urls.py
# Created on Mar 04, 2021 
# Author(s): Nitin Sharma (ns3493) <nitin.sharma@columbia.edu>

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
