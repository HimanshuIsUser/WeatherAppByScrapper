import requests
import pdb
import json
import os
import datetime
class WeatherApp:
    def __init__(self):
        self.cities = [
            "Delhi"
        ]
        self.api = "https://api.openweathermap.org/data/2.5/"
        self.api_token = "appid=5796abbde9106b7da4febfae8c44c232"
    

    def _request_for_cities_details_(self,city_name):
        request = requests.get(f'{self.api}find?q={city_name}&{self.api_token}')
        print(request.url)
        return request
    
    
def main():
    initialize_class = WeatherApp()
    for i in initialize_class.cities:
        result = initialize_class._request_for_cities_details_(i)
        file_name = f'{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.json'
        dump = json.dumps(result.json(), indent=4)
        with open(file_name,'a') as file:
            file.write(dump)
            file.close()
if __name__=='__main__':
    main()
