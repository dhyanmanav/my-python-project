# my-python-project
IBM Z DATATHON
Child Monitoring and Security System - Code Explanation:
Introduction
This Python script simulates a child monitoring system that uses a simulated heart rate monitor,
geolocation based on IP, and a database of police stations to alert guardians in case of potential
danger. If the child's heartbeat exceeds a safe threshold and the location is not one of the
pre-defined safe locations, the system provides details on nearby police stations.
1. CSV File for Police Station Data
This file path is used to load the data of police stations, containing their names, contact numbers,
and geographical coordinates. The system will use this data to find nearby police stations based on
the child's location.
2. Heartbeat Simulation
The `simulate_heartbeat()` function generates a random heartbeat between 60 and 180 bpm. This
simulated data represents the child's heartbeat for real-time monitoring.
3. Location Tracking
The `get_location()` function fetches the child's location based on their IP address using the ipapi
service. It retrieves the latitude, longitude, city, region, and country, which is later used to find
nearby police stations.
4. Police Station Data Loading
The `load_police_stations()` function loads the data of police stations from a CSV file and stores
them in a list. The stations' latitude and longitude are compared with the child's location to find
nearby police stations.
5. Distance Calculation
The `equirectangular_approximation()` function calculates the distance between two geographical
points (in kilometers). It uses an approximation to measure distance based on latitude and
longitude.
6. Monitoring and Alerts
The `monitor_child()` function simulates real-time monitoring of the child's heartbeat. If the heartbeat
exceeds a predefined threshold, an alert is triggered, displaying the child's current location and
nearby police stations.
Conclusion
This program is designed to assist guardians in monitoring a child's wellbeing by analyzing their
heartbeat and location. The system provides immediate alerts and details about nearby police
stations, helping ensure the child's safety
