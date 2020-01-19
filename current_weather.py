import weather_api 
import database 
import sys 
import pandas as pd 


def update_current_weather():
    weather_api_object = weather_api.WeatherAPI()   
    database_object = database.Database()
    
    cities_list = database_object.cities_list() 
    print (cities_list)
    
    for city_id in cities_list: 
        weather_object = weather_api_object.weather_info(city_id)
        database_object.write_weather_info(weather_object)
        

def export_to_csv(fname): 
    database_object = database.Database() 
    
    weather_list = database_object.all_weather_info()
    weather_list_df = pd.DataFrame(columns = ['city_id', 'time', 'summary', 
                                              'windSpeed', 'temperature', 
                                              'uvIndex', 'visibility'])
    
    for weather in weather_list:
        new_row = pd.Series(data={'city_id': weather.city_id, 'time': weather.time, 
                                'summary': weather.summary, 'windSpeed': weather.windSpeed, 
                                'temperature': weather.temperature, 'uvIndex': weather.uvIndex, 
                                'visibility': weather.visibility}, name='')
        
        weather_list_df = weather_list_df.append(new_row, ignore_index=False)
    
    
    print(weather_list_df)
    # exporting data into given file 
    weather_list_df.to_csv(fname)
    


def get_weather_info(city_id): 
    weather_api_obj = weather_api.WeatherAPI() 
    weather_list = weather_api_obj.weather_info_for_last_10_mins(city_id)
    
    weather_df = pd.DataFrame(columns = ['time', 'temperature'])
    
    for weather in weather_list: 
        new_row = pd.Series(data = {'time': weather.time, 'temperature': weather.temperature}, name='')
        weather_df = weather_df.append(new_row, ignore_index=False)
    
    print("Minimum temperature: " + str(weather_df['temperature'].min()))
    print("Maximum temperature: " + str(weather_df['temperature'].max()))
    print("Average temperature: " + str(round(weather_df['temperature'].mean(), 2)))

    

# main part 

if len(sys.argv) == 1:
    update_current_weather() 
else: 
    if sys.argv[1][-4:] == '.csv': 
        export_to_csv(sys.argv[1]) 
    elif sys.argv[1].isdigit(): 
        get_weather_info(int(sys.argv[1]))
        
    
        











