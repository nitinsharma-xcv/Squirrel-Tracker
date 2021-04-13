# urls.py
# Created on Mar 04, 2021 
# Author(s): Nitin Sharma (ns3493) <nitin.sharma@columbia.edu>,
#            Niharika Prasad (np2781) <niharika.prasad@columbia.edu>

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('map/', views.map_view, name='map'),
    path('sightings/', views.sightings, name='sightings'),
    path('sightings/add/', views.add, name='add'),
    path('sightings/stats/', views.stats, name='stats'),
    path('sightings/<unique_squirrel_id>/details', views.squirrel_details, name='squirrel_details'),
    path('sightings/<unique_squirrel_id>/', views.update, name='update'),
]
