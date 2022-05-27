py -m venv env
.\env\Scripts\activate

from collections.abc import Mapping
import requests
import json

# Global variables
API_KEY = 'cbd08279949548bf908279949548bf99'
Scherpenheuvel = 'IWILLE44'
Barber = 'IBOUBA1'
Fuik = 'IWILLE45'

def currentObservations(stationID, APIKEY):
    response = requests.get('https://api.weather.com/v2/pws/observations/current?stationId={}&format=json&units=m&apiKey={}'.format(stationID, APIKEY))
    if response.status_code == 200:
        response = response.json()
        observations = response['observations']
        general_atts = {}
        metrics = response['observations'][0]['metric']
        # Access the general attributes about the location - Dict
    for el in observations[-1]:
        if el != 'metric':
            general_atts[el] = observations[0][el]
        else:
            break
    return observations, metrics  
    ## 'metric' needs to be taken out of 'observations' 
