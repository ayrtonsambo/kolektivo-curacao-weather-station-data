
def Sum7DayObservations(stationID, APIKEY):
    response = requests.get('https://api.weather.com/v2/pws/dailysummary/7day?stationId={}&format=json&units=m&apiKey={}'.format(stationID, APIKEY))
    response = response.json()
    response = response['summaries']
    
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

    # Make a for loop over all the elements and append to list.
    Sum7Day_data = [process_response(i) for i in sorted(response, key = lambda x:x['obsTimeLocal'])]

    # verify if the list contains 7 days of data. 
    length = len(Sum7Day_data)
    
    #create dataset headers from sample observation
    headers = list(Sum7Day_data[0].keys())
    
    #Write data to csv
    with open('PWS_7dayObs.csv', 'w', newline = '') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = headers)
        writer.writeheader()
        writer.writerows(Sum7Day_data)
    
    # return values
    return Sum7Day_data, length
