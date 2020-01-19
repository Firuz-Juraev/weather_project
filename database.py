import sqlite3 
import settings 
import weather_class 


class Database: 
    def __init__(self):
        self.conn = sqlite3.connect(settings.DB_FILE_NAME) 
    
    
    def __del__(self):
        self.conn.close()
    
    
    def city_info(self, city_id):
        query = "SELECT lat, lon FROM cities WHERE city_id = %d" % city_id 
        c = self.conn.cursor()
        
        c.execute(query) 
        location = c.fetchone() 
        
        return location 
        
    
    def check_for_update(self, city_id, time): 
        query = "SELECT max(time) FROM weather WHERE city_id = %d" % city_id
        c = self.conn.cursor()
        
        c.execute(query) 
        max_time = c.fetchone()  
        
        if (time - max_time[0]) >= 60:
            return True 
        else:
            return False
            
        
    def write_weather_info(self, weather_object):
        
        if self.check_for_update(weather_object.city_id, weather_object.time):          
            query = """INSERT INTO weather (city_id, time, summary, windSpeed, temperature, uvIndex, visibility)
                    VALUES ('%d', '%d', '%s', '%f', '%f', '%d', '%f')""" % (weather_object.city_id, weather_object.time, 
                    weather_object.summary, weather_object.windSpeed, weather_object.temperature, weather_object.uvIndex,
                    weather_object.visibility)
                    
            c = self.conn.cursor()
            
            c.execute(query) 
            
            self.conn.commit()
        else: 
            print ("Already Up-to-date")
            
        
        
    def cities_list(self):
        query = "SELECT city_id FROM cities;" 
        
        c = self.conn.cursor()
        
        c.execute(query) 
        
        cities = [] 
        
        for city in c.fetchall():
            cities.append(city[0]) 
            
        return cities 
        
        
    