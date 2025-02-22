import requests
import pdb
import json
import os
import datetime
import csv

class WeatherApp:
    def __init__(self):
        self.cities = [
            "Delhi"
        ]
        self.api = "https://api.openweathermap.org/data/2.5/"
        self.api_token = "appid=5796abbde9106b7da4febfae8c44c232"
        self.file_name = f'{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}'
    

    def _request_for_cities_details_(self,city_name):
        request = requests.get(f'{self.api}find?q={city_name}&{self.api_token}')
        print(request.url)
        return request
    
    def _store_in_json_file(self,data):
        file_name = f'{self.file_name}.json'
        dump = json.dumps(data.json(), indent=4)
        with open(file_name,'a') as file:
            file.write(dump)
            file.close()

    def _store_in_csv_file(self,data):
        file_name = f'{self.file_name}.csv'
        with open(file_name,'a') as file:
            csv_data = csv.DictWriter(file,fieldnames=['date','city','latitude','longitude','temprature'])
            csv_data.writeheader()
            csv_data.writerows({})
            
    
def main():
    initialize_class = WeatherApp()
    for i in initialize_class.cities:
        result = initialize_class._request_for_cities_details_(i)
        data_in_json = initialize_class._store_in_csv_file(result)
        
if __name__=='__main__':
    main()
