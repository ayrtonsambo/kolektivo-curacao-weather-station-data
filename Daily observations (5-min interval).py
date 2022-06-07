from collections.abc import Mapping
import requests
import json, csv
import ipfshttpclient
import pandas as pd
import os

# Global variables : Auth keys and stationIDs
API_KEY = <API string>
Scherpenheuvel = 'IWILLE44'
Barber = 'IBOUBA1'
Fuik = 'IWILLE45'

### Daily observations - Should be run by the end of the day (obsTImeLoal == '23:59:59')
def daily5minObservations(stationID, APIKEY):
    response = requests.get('https://api.weather.com/v2/pws/observations/all/1day?stationId={}&format=json&units=m&apiKey={}'.format(stationID, APIKEY))
    response = response.json()
    response = response['observations']
    
    def process_response(response):    
        new_dict = {}
        metrics = response['metric']
        met_container = {}
        data = {}
    
        for key,val in response.items():
            if key not in data and key != 'metric':
                data[key] = response[key]
            else:
                for met, value in metrics.items():
                    met_container[met] = metrics[met]
                data.update(met_container) 
                
        return data
    
    market_data = [process_response(i) for i in response]
    length = len(market_data)
    print("This object contains data from {} observations on this day.".format(length))
    
    #create dataset headers from sample observation
    headers = list(market_data[0].keys())
    
    #Write data to csv
    with open('PWS_5minObs.csv', 'w', newline = '') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = headers)
        writer.writeheader()
        writer.writerows(market_data)
        
    return market_data
