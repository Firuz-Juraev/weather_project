import requests 
import settings 
import database 
import weather_class 

class WeatherAPI: 
    def __init__(self):
        self.api_key = settings.API_KEY
        self.link = settings.API_LINK 
        self.database_obj = database.Database()
    
    def weather_info(self, city_id): 
        lat, lon = self.database_obj.city_info(city_id) 
        request = self.link + self.api_key + "/%f,%f" % (lat, lon) + '?exclude=hourly,daily,flags'
        
        response = requests.get(request)
        
        print(response.text) 
        
        w_city_id = city_id 
        w_time = response.json()['currently']['time'] 
        w_summary = response.json()['currently']['summary'] 
        w_windSpeed = response.json()['currently']['windSpeed'] 
        w_temperature = response.json()['currently']['temperature'] 
        w_uvIndex = response.json()['currently']['uvIndex'] 
        w_visibility = response.json()['currently']['visibility'] 
        
        weather_obj = weather_class.WeatherClass(w_city_id, w_time, w_summary, 
                                                 w_windSpeed, w_temperature,
                                                 w_uvIndex, w_visibility)
        
        return weather_obj
        


