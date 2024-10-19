import time
import random
import urllib.request
import json
import csv
import math
import os

# Path to the CSV file containing police stations data
CSV_FILE_PATH = 'police_stations.csv'  # Replace with your file path

# Simulate a heart rate monitor for the child
def simulate_heartbeat():
    """Simulate heartbeat data in beats per minute (bpm)."""
    return random.randint(60,180)  # Simulated heartbeat between 60 and 180 bpm

# Check if the heartbeat exceeds the threshold
def check_heartbeat(heartbeat, threshold):
    """Check if the child's heartbeat exceeds a safe threshold."""
    return heartbeat > threshold

# Fetch location data based on IP (simplified geolocation via external API)
def get_location():
    """Simulate getting the child's location based on their IP address."""
    try:
        # Get the public IP address
        with urllib.request.urlopen('https://api64.ipify.org?format=json') as response:
            ip_data = response.read()
            ip = json.loads(ip_data)['ip']

        # Get location details using the IP address
        url = f'https://ipapi.co/{ip}/json/'
        with urllib.request.urlopen(url) as response:
            location_data = response.read()
            location_info = json.loads(location_data)
    
        return {
            'IP': ip,
            'Latitude': location_info.get('latitude'),
            'Longitude': location_info.get('longitude'),
            'City': location_info.get('city'),
            'Region': location_info.get('region'),
            'Country': location_info.get('country_name')
        }
    except Exception as e:
        return {'error': str(e)}

# Load police station data from the CSV file
def load_police_stations():
    """Load police stations from the CSV file."""
    police_stations = []
    try:
        with open('tableConvert.com_n0f29a.csv', mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                police_stations.append({
                    'Name': row['Name'],
                    'Number':row['Number'],
                    'Latitude': float(row['Latitude']),
                    'Longitude': float(row['Longitude'])
                })
    except Exception as e:
        print(f'Error loading police stations data: {str(e)}')
    return police_stations
def equirectangular_approximation(lat1, lon1, lat2, lon2):
         # Convert degrees to radians
         lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
     
         # Differences in latitude and longitude
         dlat = lat2 - lat1
         dlon = lon2 - lon1
    
         # Approximate using the equirectangular projection
         b = dlat**2 + (math.cos((lat1 + lat2) / 2) * dlon)**2
         R = 6371.0  # Radius of Earth in kilometers
         distance = R * math.sqrt(b)
    
         return distance


def display(purpose,latitude,longitude):
     print('ur child is in',purpose,'location')
     print('latitude of',purpose,'location is',latitude)
     print('longitude of',purpose,'location is',longitude)
     return 0        
     

# Find nearest police stations based on the child's location
def find_nearest_police_stations(lat, lon, police_stations,location_info):
    """Find nearest police stations within a certain distance."""
    child_location = (lat, lon)
    nearby_stations = []

    # Calculate distance to each police station and check if it's within 1500 meters


    for station in police_stations:
         station_location = (station['Latitude'], station['Longitude'])

         distance = equirectangular_approximation(lat, lon, station['Latitude'], station['Longitude'])
         if distance<=10:
             nearby_stations.append(station['Name'])
             nearby_stations.append(station['Number'])
    


    return nearby_stations

    
# Display a message when the heartbeat exceeds the threshold
def display_message(heartbeat, location_info, police_stations):
    """Print a message to the console with heartbeat, location, and police station details."""
    message = f"""
    ALERT! Your child's heartbeat is {heartbeat} bpm, which exceeds the safe threshold.
    
    Child's Location:
    - City: {location_info.get('City')}
    - Region: {location_info.get('Region')}
    - Country: {location_info.get('Country')}
    - Latitude: {location_info.get('Latitude')}
    - Longitude: {location_info.get('Longitude')}
    
    Nearest Police Stations:
    {'; '.join(police_stations) if police_stations else 'No police stations found.'}

    Please check on them immediately.
    """
    print(message)


# Main program to simulate tracking and alert system
def monitor_child(heartbeat_threshold, monitoring_duration):
    """Monitor the child's heartbeat and display a message if limit is exceeded."""
    start_time = time.time()
    
    # Load police station data from CSV
    police_stations = load_police_stations()
    
    while (time.time() - start_time) < monitoring_duration:
        # Simulate the child's heartbeat
        heartbeat = simulate_heartbeat()
        print(f"Current heartbeat: {heartbeat} bpm")
        time.sleep(3)
        os.system("cls")
        
        
        # Check if the heartbeat exceeds the threshold
        if check_heartbeat(heartbeat, heartbeat_threshold):
            # make sound
            
            # Get the child's location
            location_info = get_location()
            # Get nearest police stations from the loaded data
            lat = location_info.get('Latitude')
            lon = location_info.get('Longitude')
            
            
            nearby_police_stations = find_nearest_police_stations(lat, lon, police_stations,location_info)
            # Display the alert message with heartbeat, location, and police station details
            display_message(heartbeat, location_info, nearby_police_stations)
            winsound.Beep(1000, 500)
            time.sleep(10)
            
        
        # Sleep for a short time before the next check (simulating real-time monitoring)
        time.sleep(1)  # Check every 3 seconds
        

if __name__ == "__main__":
     HEARTBEAT_THRESHOLD = 120  # Set safe heartbeat limit
     MONITORING_DURATION = 60  # Monitor for 60 seconds (can change)
     # Get the child's location
     location_info = get_location()
     # Get nearest police stations from the loaded data
     lat = location_info.get('Latitude')
     lon = location_info.get('Longitude')
     print('|                     welcome to Child security system                  |')
     time.sleep(2)
     print('|    please give the locations of the child in which it would be safe   |')
     time.sleep(2)
     print('|                    and you will only be given a warning               |')
     time.sleep(2)
     print('|  else an alert message will be given which will give all the details  |')
     time.sleep(2)
     print('enter how many locations u want to add: ')
     a=int(input('if not give 0:'))
     for i in range(0,a):
         print('enter the name of ',i+1,'location: ')
         purpose=input()
         print('enter',i+1,'latitude: ')
         latitude=float(input())
         print('enter',i+1,'longitude: ')
         longitude=float(input())
         distance_2 = equirectangular_approximation(lat, lon, latitude, longitude)
       
         if distance_2<=1:
             P=purpose
             L=float(latitude)
             Lo=float(longitude)
             
             break
     if a==0:
         distance_2=100  
     if distance_2<=1:   
         """Monitor the child's heartbeat and display a message if limit is exceeded."""
         start_time = time.time()
         while (time.time() - start_time) <  MONITORING_DURATION:
              # Simulate the child's heartbeat
             heartbeat = simulate_heartbeat()
             print(f"Current heartbeat: {heartbeat} bpm")
             time.sleep(3)
             os.system("cls")
             
             if check_heartbeat(heartbeat, HEARTBEAT_THRESHOLD ):
                 display(P,L,Lo)
                 time.sleep(10)
                 break
                 
             time.sleep(1) 
         print('your child is in ur given location so take care')    
         
     else:
         monitor_child( HEARTBEAT_THRESHOLD,MONITORING_DURATION)
         


    



