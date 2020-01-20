import requests 
import settings 
import database 
import weather_class 

class WeatherAPI: 
    def __init__(self):
        self.api_key = settings.API_KEY
        self.link = settings.API_LINK 
        self.database_obj = database.Database() 
        
   #This function gets city_id and optinal time as parameter and returns WeatherClass object      
    def weather_info(self, city_id, time=''): 
        lat, lon = self.database_obj.city_info(city_id) 
        request = self.link + self.api_key + "/%f,%f" % (lat, lon) + time + '?exclude=hourly,daily,flags'
        
        response = requests.get(request)
        
        
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
    
    
    # This function retrives 10 temperatures for last 10 minutes and returns all of them as list of WeatherClass objects 
    def weather_info_for_last_10_mins(self, city_id): 
        weather_list = []
        weather_object = self.weather_info(city_id) 
        current_time = weather_object.time
        
        weather_list.append(weather_object)
        
        for i in range(1,10): 
            weather_list.append(self.weather_info(city_id, "," + str(current_time-i*60) ))
        
        return weather_list 
        
