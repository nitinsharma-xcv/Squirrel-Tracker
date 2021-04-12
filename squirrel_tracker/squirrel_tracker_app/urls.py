# urls.py
# Created on Mar 04, 2021 
# Author(s): Nitin Sharma (ns3493) <nitin.sharma@columbia.edu>,
#            Niharika Prasad (np2781) <niharika.prasad@columbia.edu>

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sightings/', views.list_of_squirrels, name='list_of_squirrels'),
]
