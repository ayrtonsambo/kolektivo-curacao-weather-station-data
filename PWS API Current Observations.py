from collections.abc import Mapping
import requests
import json

# Global variables
API_KEY = <API string>
Scherpenheuvel = 'IWILLE44'
Barber = 'IBOUBA1'
Fuik = 'IWILLE45'

### Current observations
def currentObservations(stationID, APIKEY):
    
    response = requests.get('https://api.weather.com/v2/pws/observations/current?stationId={}&format=json&units=m&apiKey={}'.format(stationID, APIKEY))
    
    if response.status_code == 200:
        response = response.json()
        observations = response['observations']
        metrics = response['observations'][0]['metric']
        del observations[0]['metric']
    else:
        pass
        print('API Request Unsuccesful')
        
    new_dict = {}
    market_data = {}
    
    for key,val in observations[0].items():
        if key not in market_data:
            market_data[key] = observations[0][key]
            
    for met, value in metrics.items():
        new_dict[met] = metrics[met]
        market_data.update(new_dict)  

    # Write data to csv - #2
    headers = list(market_data.keys())

    with open('csv_test1.csv', 'w', newline = '') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = headers)
        writer.writeheader()
        writer.writerow(market_data)

    return market_data  

currentObservations(Barber, API_KEY)

