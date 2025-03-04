import requests
import pdb
import json
import os
import datetime
import csv
import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="",database='WeatherApp')

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
            csv_data = csv.DictWriter(file,fieldnames=['lat','lon', 'name', 'temp', 'feels_like', 'temp_min', 'temp_max', 'pressure', 'humidity', 'sea_level', 'grnd_level'])
            csv_data.writeheader()
            csv_data.writerows([data])

    def extract_valid_data(self,data):
        content = data.json()
        formated_data = content['list'][0]['coord']
        formated_data = formated_data | {'name':content['list'][0]['name']}
        formated_data = formated_data | content['list'][0]['main']
        return formated_data

    def _store_data_in_db(self,data):
        cursorObject = mydb.cursor()
        value_list = [j for k, j in data.items()]
        query = "INSERT INTO weatherData (lat,lon, city_name, temp, feels_like, temp_min, temp_max, pressure, humidity, sea_level, grnd_level)\
VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s)"

        cursorObject.execute(query, value_list)
        mydb.commit()
        return 'Done'

def main():
    initialize_class = WeatherApp()
    for i in initialize_class.cities:
        result = initialize_class._request_for_cities_details_(i)
        clean_data = initialize_class.extract_valid_data(result)
        initialize_class._store_data_in_db(clean_data)
        initialize_class._store_data_in_db(clean_data)
        
if __name__=='__main__':
    main()
