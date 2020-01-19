import weather_api 
import database 

import pandas as pd 


def update_current_weather():
    weather_api_object = weather_api.WeatherAPI()   
    database_object = database.Database()
    
    cities_list = database_object.cities_list() 
    print (cities_list)
    
    for city_id in cities_list: 
        weather_object = weather_api_object.weather_info(city_id)
        database_object.write_weather_info(weather_object)
        

def export_to_csv(): 
    

#update_current_weather()