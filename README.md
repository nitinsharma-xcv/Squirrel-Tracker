# IEOR E4501: Tools for Analytics Project
# Squirrel-Tracker

## Introduction
The project is a web application, developed with Django framework of Python. In this application, user can import the 2018 Central Park Squirrel Census data and add, update, and view squirrel data

Developed using Python 3.8.8

## Background
Eccentric billionaire Joffrey Hosencratz just purchased the web development company you work for. You’ve met him once in an elevator and he was impressed with your skill in developing web applications with the ``Django`` framework. He also relayed that his most recent trip to Sedona, AZ has left him in a bit of trouble. See, he fancies the show Rick and Morty and a particular scene coupled with a traumatic childhood squirrel experience and a bad crystal bath experience in Sedona as left him wanting. 

He would like to start keeping track of all the known squirrels and plans to start with Central Park. He’s asked you to build an application that can import the 2018 Central Park Squirrel Census data and allow his team to add, update, and view squirrel data. 

### DataSet
In this project, [**2018 Central Park Squirrel Census**](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw) dataset is used.

### Features
The project should be Django based should have the following features:

-	Management commands:

  Import: A command that can be used to import the data from the 2018 census file (in CSV format). The file path should be specified at the command line after the name of the management command. 
  
  ```$ python manage.py import_squirrel_data <file_path>```

  Export: A command that can be used to export the data in CSV format. The file path should be specified at the command line after the name of the management command. 
  
  ```$ python manage.py export_squirrel_data <file_path>```


-	Views:

	 - A view that shows a map that displays the location of the squirrel sightings on an OpenStreets map.
	 - A view that lists all squirrel sightings with links to view each sighting
	 - A view to update a particular sighting
	 - A view to create a new sighting
	 - A view with general stats about the sightings


## Server Application Link:
   - Home: https://squirreltracker-ns3493-np2781.uk.r.appspot.com
   - Sightings: https://squirreltracker-ns3493-np2781.uk.r.appspot.com/sightings/
   - Map: https://squirreltracker-ns3493-np2781.uk.r.appspot.com/map/
   - Add new sighting: https://squirreltracker-ns3493-np2781.uk.r.appspot.com/sightings/add/
   - Edit a particular sighting: https://squirreltracker-ns3493-np2781.uk.r.appspot.com/sightings/ {Unique Squirrel ID}/
   - Stats of sightings: https://squirreltracker-ns3493-np2781.uk.r.appspot.com/sightings/stats/



## Contributors

### Project Group 27
UNIs: [np2781, ns3493]

Alphabetical list of Contributors:

 - Niharika Prasad (np2781)

 - Nitin Sharma (ns3493)
