import requests

class WeatherApp:
    def __init__(self):
        self.cities = [
            "New York City", "London", "Paris", "Tokyo", "Sydney", 
            "Dubai", "Rome", "Los Angeles", "Beijing", "Rio de Janeiro",
            "Toronto", "Singapore", "Moscow", "Cape Town", "Bangkok",
            "Barcelona", "Berlin", "Istanbul", "Hong Kong", "Amsterdam",
            "San Francisco", "Seoul", "Mumbai", "Shanghai", "Vienna",
            "Madrid", "Chicago", "Lisbon", "Kuala Lumpur", "Prague"
        ]
        self.api = "https://api.openweathermap.org/data/2.5/"
        self.api_token = "appid=5796abbde9106b7da4febfae8c44c232"
    

    def _request_for_cities_details_(self,city_name):
        request = requests.get(f'{self.api}find?d={city_name}&{self.api_token}')
        return request
    
    
def main():
    initialize_class = WeatherApp()
    
if __name__=='__main__':
    main()
